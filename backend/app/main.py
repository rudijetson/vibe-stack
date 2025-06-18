from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from app.api.router import api_router
from app.core.config import settings
from app.core.rate_limiter import limiter

app = FastAPI(
    title="Vibe Stack Backend",
    description="AI-First Full-Stack Template API",
    version="0.1.0",
)

# Add rate limiter
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


# Custom middleware to handle OPTIONS requests properly
class OptionsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.method == "OPTIONS":
            return Response(status_code=200)
        return await call_next(request)


# Add OPTIONS middleware first
app.add_middleware(OptionsMiddleware)

# Set up CORS - Expanded configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", *settings.CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["Content-Type", "Authorization", "Accept", "Origin", "X-Requested-With", "X-CSRF-Token"],
    expose_headers=["Content-Type", "Authorization"],
    max_age=600,  # 10 minutes cache for preflight requests
)

# Include API router
app.include_router(api_router, prefix="/api")


@app.get("/")
async def root():
    """Health check endpoint."""
    from app.core.demo import demo_service
    
    return {
        "status": "online", 
        "environment": settings.ENVIRONMENT, 
        "version": "0.1.0",
        "demo_mode": demo_service.is_demo_mode(settings.SUPABASE_URL, settings.OPENAI_API_KEY, settings.DEMO_MODE),
        "features": {
            "auth": bool(settings.SUPABASE_URL and settings.SUPABASE_URL != "demo"),
            "ai": bool(settings.OPENAI_API_KEY or settings.ANTHROPIC_API_KEY),
            "rate_limiting": True
        }
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=settings.ENVIRONMENT == "development")
