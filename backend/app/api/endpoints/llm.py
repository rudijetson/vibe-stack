from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import logging
from typing import Optional

from app.services.llm.llm_service import LLMService, get_llm_service
from app.services.llm.embedding_service import EmbeddingService, get_embedding_service
from app.models.llm import TextGenerationRequest, TextGenerationResponse, EmbeddingRequest, EmbeddingResponse
from app.services.supabase.auth import SupabaseAuthService, get_auth_service
from app.core.config import settings
from app.core.demo import demo_service

router = APIRouter()
security = HTTPBearer()  # Make authentication required
logger = logging.getLogger(__name__)

# Import rate limiter
from app.core.rate_limiter import limiter


@router.post("/demo", response_model=dict)
@limiter.limit("10/minute")
async def demo_generate(request_data: dict, request: Request):
    """Demo endpoint that works without authentication or API keys."""
    try:
        prompt = request_data.get("prompt", "Hello from the Vibe Stack!")
        model = request_data.get("model", "demo")
        
        # Check if we're in demo mode
        if demo_service.is_demo_mode(settings.SUPABASE_URL, settings.OPENAI_API_KEY, settings.DEMO_MODE):
            response = demo_service.mock_llm_response(prompt, model)
            return {
                "content": response["content"],
                "model": response["model"],
                "demo": True,
                "message": "🌟 Demo mode active! Add your API keys to use real AI services."
            }
        
        # If we have real API keys, use the real service
        return {
            "content": "Real API integration is available. Use the /generate endpoint with authentication.",
            "demo": False
        }
        
    except Exception as e:
        logger.error(f"Demo generation error: {str(e)}")
        return {
            "content": "Demo mode is working! This shows how AI integration works in the Vibe Stack.",
            "model": "demo",
            "demo": True,
            "error": str(e)
        }


@router.post("/generate", response_model=TextGenerationResponse)
@limiter.limit("30/minute")
async def generate_text(
    request: TextGenerationRequest,
    credentials: HTTPAuthorizationCredentials = Depends(security),
    auth_service: SupabaseAuthService = Depends(get_auth_service),
    # We will override this service based on the request provider
    llm_service: LLMService = Depends(lambda: get_llm_service("openai")),
):
    """Generate text using the specified LLM model."""
    try:
        # Log request details for debugging
        logger.info(f"Sameer Received text generation request with model: {request}, provider: {credentials}")

        # Validate user authentication
        try:
            user = await auth_service.get_user(credentials.credentials)
            logger.info(f"User authenticated: {user.email if hasattr(user, 'email') else 'Unknown user'}")
        except Exception as auth_error:
            logger.error(f"Authentication error: {str(auth_error)}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Authentication failed: {str(auth_error)}",
                headers={"WWW-Authenticate": "Bearer"},
            )

        # Get the right LLM service based on provider
        try:
            if request.provider:
                llm_service = get_llm_service(request.provider)
                logger.info(f"Using LLM provider: {request.provider}")
        except ValueError as provider_error:
            logger.error(f"Provider error: {str(provider_error)}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(provider_error))

        # Generate text with the LLM service
        try:
            logger.info(f"Generating text with prompt: {request.prompt[:50]}...")

            # Check if API keys are configured
            if request.provider == "openai" and not settings.OPENAI_API_KEY:
                raise ValueError("OpenAI API key not configured. Please set the OPENAI_API_KEY environment variable.")
            elif request.provider == "anthropic" and not settings.ANTHROPIC_API_KEY:
                raise ValueError("Anthropic API key not configured. Please set the ANTHROPIC_API_KEY environment variable.")

            response = await llm_service.generate_text(
                prompt=request.prompt, model=request.model, max_tokens=request.max_tokens, temperature=request.temperature
            )
            logger.info(f"Text generation successful, response length: {len(response.text)}")
            return TextGenerationResponse(text=response.text, model=response.model, usage=response.usage)
        except Exception as generation_error:
            logger.error(f"Text generation error: {str(generation_error)}", exc_info=True)
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Text generation failed: {str(generation_error)}")

    except HTTPException:
        # Re-raise HTTP exceptions so they maintain their status codes
        raise
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Unexpected error: {str(e)}")


@router.post("/embedding", response_model=EmbeddingResponse)
async def create_embedding(
    request: EmbeddingRequest,
    credentials: HTTPAuthorizationCredentials = Depends(security),
    auth_service: SupabaseAuthService = Depends(get_auth_service),
    embedding_service: EmbeddingService = Depends(get_embedding_service),
):
    """Create an embedding vector for the provided text."""
    try:
        # Validate user authentication
        try:
            user = await auth_service.get_user(credentials.credentials)
            logger.info(f"User authenticated: {user.email if hasattr(user, 'email') else 'Unknown user'}")
        except Exception as auth_error:
            logger.error(f"Authentication error: {str(auth_error)}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Authentication failed: {str(auth_error)}",
                headers={"WWW-Authenticate": "Bearer"},
            )

        # Generate embedding with the embedding service
        embedding = await embedding_service.create_embedding(text=request.text, model=request.model)

        return EmbeddingResponse(embedding=embedding.embedding, model=embedding.model, usage=embedding.usage)
    except Exception as e:
        logger.error(f"Embedding creation failed: {str(e)}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Embedding creation failed: {str(e)}")
