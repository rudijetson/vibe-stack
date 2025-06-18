"""
AI Models Configuration
Contains all available models with descriptions, pricing, and capabilities
"""

from enum import Enum
from typing import Dict, List, Any
from pydantic import BaseModel


class ModelTier(str, Enum):
    PREMIUM = "premium"
    NEXT_TIER = "next_tier"
    BUDGET = "budget"


class ModelCapability(str, Enum):
    TEXT_GENERATION = "text_generation"
    REASONING = "reasoning"
    CODING = "coding"
    MULTIMODAL = "multimodal"
    LONG_CONTEXT = "long_context"
    FAST_RESPONSE = "fast_response"
    TOOL_USE = "tool_use"


class ModelConfig(BaseModel):
    name: str
    display_name: str
    provider: str
    tier: ModelTier
    input_price_per_million: float  # USD per million tokens
    output_price_per_million: float  # USD per million tokens
    max_tokens: int
    context_window: int
    capabilities: List[ModelCapability]
    description: str
    best_for: List[str]
    speed_rating: int  # 1-5, where 5 is fastest
    accuracy_rating: int  # 1-5, where 5 is most accurate
    cost_rating: int  # 1-5, where 5 is most cost-effective
    available: bool = True


# All available models
MODELS: Dict[str, ModelConfig] = {
    # OpenAI Models
    "o3-pro": ModelConfig(
        name="o3-pro",
        display_name="OpenAI o3 Pro",
        provider="openai",
        tier=ModelTier.PREMIUM,
        input_price_per_million=20.0,
        output_price_per_million=80.0,
        max_tokens=8192,
        context_window=128000,
        capabilities=[ModelCapability.REASONING, ModelCapability.CODING, ModelCapability.TOOL_USE, ModelCapability.LONG_CONTEXT],
        description="Highest reasoning capability, best for complex tasks, slower but most accurate",
        best_for=["Research", "Advanced coding", "Complex analysis", "Business intelligence"],
        speed_rating=2,
        accuracy_rating=5,
        cost_rating=1,
    ),
    
    "o3": ModelConfig(
        name="o3",
        display_name="OpenAI o3",
        provider="openai",
        tier=ModelTier.NEXT_TIER,
        input_price_per_million=10.0,
        output_price_per_million=40.0,
        max_tokens=8192,
        context_window=128000,
        capabilities=[ModelCapability.REASONING, ModelCapability.CODING, ModelCapability.TOOL_USE, ModelCapability.LONG_CONTEXT],
        description="Advanced reasoning, cost-efficient, high-throughput",
        best_for=["Production apps", "Coding", "General AI tasks", "Content analysis"],
        speed_rating=3,
        accuracy_rating=4,
        cost_rating=2,
    ),
    
    "o3-mini": ModelConfig(
        name="o3-mini",
        display_name="OpenAI o3 Mini",
        provider="openai",
        tier=ModelTier.NEXT_TIER,
        input_price_per_million=2.0,
        output_price_per_million=8.0,
        max_tokens=4096,
        context_window=64000,
        capabilities=[ModelCapability.REASONING, ModelCapability.CODING, ModelCapability.FAST_RESPONSE],
        description="Fast, cost-efficient reasoning model, good balance of speed and capability",
        best_for=["High-volume tasks", "Real-time processing", "Cost-sensitive applications"],
        speed_rating=4,
        accuracy_rating=4,
        cost_rating=4,
    ),
    
    "o4-mini": ModelConfig(
        name="o4-mini",
        display_name="OpenAI o4 Mini",
        provider="openai",
        tier=ModelTier.BUDGET,
        input_price_per_million=1.10,
        output_price_per_million=4.40,
        max_tokens=4096,
        context_window=64000,
        capabilities=[ModelCapability.TEXT_GENERATION, ModelCapability.FAST_RESPONSE, ModelCapability.TOOL_USE],
        description="Fastest and most cost-effective OpenAI model, good for high-volume use",
        best_for=["Chatbots", "High-volume processing", "Simple tasks", "Real-time applications"],
        speed_rating=5,
        accuracy_rating=3,
        cost_rating=5,
    ),
    
    # Anthropic Models
    "claude-opus-4-20250514": ModelConfig(
        name="claude-opus-4-20250514",
        display_name="Claude Opus 4",
        provider="anthropic",
        tier=ModelTier.PREMIUM,
        input_price_per_million=15.0,
        output_price_per_million=75.0,
        max_tokens=8192,
        context_window=200000,
        capabilities=[ModelCapability.REASONING, ModelCapability.CODING, ModelCapability.LONG_CONTEXT, ModelCapability.TEXT_GENERATION],
        description="Flagship model, best for deep reasoning, advanced coding, highest accuracy",
        best_for=["Research", "Automation", "Agentic AI", "Complex writing", "Advanced analysis"],
        speed_rating=2,
        accuracy_rating=5,
        cost_rating=1,
    ),
    
    "claude-3-5-sonnet-20241022": ModelConfig(
        name="claude-3-5-sonnet-20241022",
        display_name="Claude Sonnet 4",
        provider="anthropic",
        tier=ModelTier.NEXT_TIER,
        input_price_per_million=3.0,
        output_price_per_million=15.0,
        max_tokens=8192,
        context_window=200000,
        capabilities=[ModelCapability.TEXT_GENERATION, ModelCapability.CODING, ModelCapability.LONG_CONTEXT, ModelCapability.FAST_RESPONSE],
        description="Balanced performance and cost, high-throughput, strong coding abilities",
        best_for=["Content generation", "Support bots", "Business applications", "Coding assistance"],
        speed_rating=4,
        accuracy_rating=4,
        cost_rating=3,
    ),
    
    "claude-3-haiku-20240307": ModelConfig(
        name="claude-3-haiku-20240307",
        display_name="Claude Haiku",
        provider="anthropic",
        tier=ModelTier.BUDGET,
        input_price_per_million=0.25,
        output_price_per_million=1.25,
        max_tokens=4096,
        context_window=200000,
        capabilities=[ModelCapability.TEXT_GENERATION, ModelCapability.FAST_RESPONSE],
        description="Lightweight, fastest Claude model, optimized for efficiency and throughput",
        best_for=["Routine tasks", "Customer support", "Simple queries", "High-volume processing"],
        speed_rating=5,
        accuracy_rating=3,
        cost_rating=5,
    ),
    
    # Google Gemini Models
    "gemini-2.5-pro": ModelConfig(
        name="gemini-2.5-pro",
        display_name="Gemini 2.5 Pro",
        provider="gemini",
        tier=ModelTier.PREMIUM,
        input_price_per_million=7.0,  # Estimated enterprise pricing
        output_price_per_million=21.0,
        max_tokens=8192,
        context_window=1000000,
        capabilities=[ModelCapability.MULTIMODAL, ModelCapability.REASONING, ModelCapability.CODING, ModelCapability.LONG_CONTEXT],
        description="Deep Think, multimodal capabilities, 1M token context, top benchmarks",
        best_for=["Coding", "Complex reasoning", "Multimodal applications", "Enterprise use"],
        speed_rating=3,
        accuracy_rating=5,
        cost_rating=2,
    ),
    
    "gemini-2.5-flash": ModelConfig(
        name="gemini-2.5-flash",
        display_name="Gemini 2.5 Flash",
        provider="gemini",
        tier=ModelTier.NEXT_TIER,
        input_price_per_million=0.50,  # Estimated
        output_price_per_million=1.50,
        max_tokens=8192,
        context_window=1000000,
        capabilities=[ModelCapability.FAST_RESPONSE, ModelCapability.REASONING, ModelCapability.LONG_CONTEXT],
        description="Fastest Gemini model, high-volume efficient, strong reasoning",
        best_for=["Real-time applications", "Chatbots", "Customer service", "High-throughput"],
        speed_rating=5,
        accuracy_rating=4,
        cost_rating=5,
    ),
    
    "gemini-1.5-pro": ModelConfig(
        name="gemini-1.5-pro",
        display_name="Gemini 1.5 Pro",
        provider="gemini",
        tier=ModelTier.BUDGET,
        input_price_per_million=3.5,
        output_price_per_million=10.5,
        max_tokens=8192,
        context_window=128000,
        capabilities=[ModelCapability.MULTIMODAL, ModelCapability.REASONING, ModelCapability.CODING],
        description="Previous generation Pro model, still very capable, more affordable",
        best_for=["General applications", "Cost-conscious projects", "Multimodal tasks"],
        speed_rating=3,
        accuracy_rating=4,
        cost_rating=4,
    ),
}


# Default models by provider (cheapest available)
DEFAULT_MODELS = {
    "openai": "o4-mini",
    "anthropic": "claude-3-haiku-20240307", 
    "gemini": "gemini-2.5-flash",
}

# Task-specific model recommendations
TASK_RECOMMENDATIONS = {
    "transcript_processing": {
        "budget": "claude-3-haiku-20240307",
        "balanced": "claude-3-5-sonnet-20241022",
        "premium": "claude-opus-4-20250514",
    },
    "outline_generation": {
        "budget": "gemini-2.5-flash",
        "balanced": "o3-mini",
        "premium": "o3-pro",
    },
    "slide_generation": {
        "budget": "gemini-1.5-pro",
        "balanced": "gemini-2.5-pro",
        "premium": "claude-opus-4-20250514",
    },
    "reasoning_tasks": {
        "budget": "o4-mini",
        "balanced": "o3-mini",
        "premium": "o3-pro",
    },
}


def get_models_by_provider(provider: str) -> List[ModelConfig]:
    """Get all models for a specific provider."""
    return [model for model in MODELS.values() if model.provider == provider]


def get_models_by_tier(tier: ModelTier) -> List[ModelConfig]:
    """Get all models for a specific tier."""
    return [model for model in MODELS.values() if model.tier == tier]


def get_cheapest_models() -> Dict[str, ModelConfig]:
    """Get the cheapest available model for each provider."""
    cheapest = {}
    for provider in ["openai", "anthropic", "gemini"]:
        provider_models = get_models_by_provider(provider)
        if provider_models:
            cheapest[provider] = min(
                provider_models, 
                key=lambda m: m.input_price_per_million + m.output_price_per_million
            )
    return cheapest


def get_model_for_task(task: str, budget_level: str = "budget") -> str:
    """Get recommended model for a specific task and budget level."""
    if task in TASK_RECOMMENDATIONS and budget_level in TASK_RECOMMENDATIONS[task]:
        return TASK_RECOMMENDATIONS[task][budget_level]
    # Fallback to cheapest available
    provider_defaults = get_cheapest_models()
    return list(provider_defaults.values())[0].name if provider_defaults else "o4-mini"


def get_all_models_info() -> Dict[str, Any]:
    """Get comprehensive information about all models for frontend."""
    return {
        "models": {name: model.dict() for name, model in MODELS.items()},
        "providers": {
            provider: [model.name for model in get_models_by_provider(provider)]
            for provider in ["openai", "anthropic", "gemini"]
        },
        "tiers": {
            tier.value: [model.name for model in get_models_by_tier(tier)]
            for tier in ModelTier
        },
        "defaults": DEFAULT_MODELS,
        "task_recommendations": TASK_RECOMMENDATIONS,
        "cheapest": {provider: model.name for provider, model in get_cheapest_models().items()},
    }