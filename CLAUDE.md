# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a full-stack web application template with:
- **Frontend**: Next.js 14 with TypeScript, Tailwind CSS, and Supabase integration
- **Backend**: Python FastAPI with async support
- **Database**: Supabase (PostgreSQL) with migrations
- **Infrastructure**: Docker-based development and production environments

## Essential Commands

### Development
```bash
# Start full development environment (recommended)
make dev

# Start individual services
make dev-frontend  # Frontend only on port 3000
make dev-backend   # Backend only on port 8000

# Access services
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

### LLM API Testing
The system supports 10 LLM models across 3 providers with comprehensive testing capabilities:

```bash
# Test model information endpoints
curl http://localhost:8000/api/models/info
curl http://localhost:8000/api/models/defaults
curl http://localhost:8000/api/models/cheapest

# Test demo endpoint (no auth required)
curl -X POST http://localhost:8000/api/llm/demo \
  -H "Content-Type: application/json" \
  -d '{"prompt":"Hello!", "model":"demo"}'

# Test authenticated endpoints (requires auth token)
curl -X POST http://localhost:8000/api/llm/generate \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"prompt":"Hello!", "model":"o4-mini", "provider":"openai"}'
```

### Production
```bash
make prod           # Start production environment
make prod-frontend  # Frontend production only
make prod-backend   # Backend production only
```

### Database Migrations
```bash
# Create new migration
make db-migration-new name=your_migration_name

# Apply migrations to remote database
make db-apply

# Check migration status
make db-status
```

### Build and Installation
```bash
# Frontend
make install-frontend  # Install dependencies locally
make build-frontend    # Build for production

# Backend
make install-backend   # Install dependencies locally

# Cleanup
make clean            # Remove containers and volumes
```

### Testing and Linting
**Note**: Testing infrastructure is not fully configured. When implementing tests:
- Frontend: Consider adding Jest/Vitest to package.json
- Backend: Add pytest to requirements.txt (Makefile already has `make test` command)
- Backend linting: Add flake8, black, isort to requirements.txt (Makefile has `make lint` command)

## Architecture and Key Patterns

### Frontend Structure
- **App Router**: Uses Next.js 14 App Router in `frontend/app/`
- **Components**: Reusable UI components in `frontend/components/`
- **Services**: API communication layer in `frontend/services/`
- **Styling**: Tailwind CSS with custom configuration
- **Type Safety**: TypeScript with path aliasing (`@/*` maps to `frontend/*`)

### Backend Structure
- **API Endpoints**: FastAPI routes in `backend/app/api/endpoints/`
- **Service Layer**: Business logic in `backend/app/services/`
  - `llm/`: Multi-LLM integrations (OpenAI, Anthropic, Google Gemini)
  - `supabase/`: Database and auth services
  - `vectordb/`: Vector database operations
- **Models**: Pydantic models in `backend/app/models/`
- **Core**: Configuration and utilities in `backend/app/core/`
- **Config**: Model definitions and configurations in `backend/app/config/`

### LLM Integration Architecture
The system provides comprehensive LLM support with:

**Supported Models (10 total):**
- **OpenAI**: o3-pro, o3, o3-mini, o4-mini
- **Anthropic**: claude-opus-4, claude-3-5-sonnet, claude-3-haiku  
- **Google Gemini**: gemini-2.5-pro, gemini-2.5-flash, gemini-1.5-pro

**Key Components:**
- `backend/app/services/llm/llm_service.py` - Main LLM service implementations
- `backend/app/services/llm/embedding_service.py` - Text embedding services
- `backend/app/config/models.py` - Comprehensive model configurations with pricing, capabilities, and recommendations
- `backend/app/api/endpoints/llm.py` - LLM API endpoints with authentication and rate limiting

**Features:**
- **Smart Model Selection**: Task-specific recommendations and tier-based pricing
- **Demo Mode**: Test integration without API keys
- **Error Handling**: Graceful degradation and comprehensive error responses
- **Rate Limiting**: 10/min for demo, 30/min for authenticated endpoints
- **Authentication**: Bearer token validation via Supabase Auth

### Authentication Flow
- Supabase Auth handles all authentication
- Multiple providers: Google, LinkedIn, Email/Password
- Auth pages: `/auth/login`, `/auth/callback`, `/auth/reset-password`
- Protected routes use Supabase session management

### API Integration Pattern
1. Frontend services make requests to backend API
2. Backend validates requests using Pydantic models
3. Backend services handle business logic
4. Responses are type-safe on both ends

### Environment Configuration
Two `.env` files are required:
- `.env`: Backend environment variables
- `frontend/.env.local`: Frontend environment variables

**Required for authentication:**
- `SUPABASE_URL`, `SUPABASE_ANON_KEY`, `SUPABASE_SERVICE_KEY`

**Optional for AI features (any combination):**
- `OPENAI_API_KEY` - Enables OpenAI models (o3-pro, o3, o3-mini, o4-mini)
- `ANTHROPIC_API_KEY` - Enables Anthropic models (claude-opus-4, claude-3-5-sonnet, claude-3-haiku)  
- `GEMINI_API_KEY` - Enables Google Gemini models (gemini-2.5-pro, gemini-2.5-flash, gemini-1.5-pro)

**Demo Mode**: If no valid API keys are provided, the system automatically enables demo mode with mock AI responses.

## Development Guidelines

### When Adding Features
1. **Frontend Components**: Follow existing patterns in `components/`
2. **API Endpoints**: Add to `backend/app/api/endpoints/` with proper Pydantic models
3. **Database Changes**: Create migrations using `make db-migration-new`
4. **Environment Variables**: Update both `.env.example` files if adding new keys

### Code Conventions
- Frontend: Follow Next.js and React best practices
- Backend: Follow FastAPI patterns with async/await
- Use existing service abstractions (don't directly call external APIs)
- Maintain separation between API endpoints and business logic

### Common Development Tasks
- **Add new API endpoint**: Create in `backend/app/api/endpoints/`, add router to `main.py`
- **Add new page**: Create in `frontend/app/` following Next.js App Router conventions
- **Add database table**: Create migration with `make db-migration-new`, define schema in SQL
- **Add new LLM provider**: Extend `backend/app/services/llm/` following existing patterns

## Important Notes
- Hot-reload is enabled in development for both frontend and backend
- API documentation is auto-generated at `/docs`
- Vector database has in-memory fallback if Qdrant is not configured
- All authentication flows are handled by Supabase (don't implement custom auth)