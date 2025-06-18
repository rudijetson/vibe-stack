# 🌟 Vibe Stack - AI-First Full-Stack Template

A modern, production-ready template for building web applications with AI integration. Perfect for developers who want to build with AI assistance or integrate LLM features.

## ✨ What's Included

- 🎨 **Next.js 14** - Modern React framework with App Router
- 🐍 **FastAPI** - High-performance Python backend
- 🔐 **Supabase Auth** - Complete authentication system
- 🧠 **Multi-LLM Integration** - OpenAI, Anthropic Claude, Google Gemini support
- 🎨 **Tailwind CSS** - Utility-first styling
- 🐳 **Docker** - Containerized development
- 📊 **Vector Database** - Semantic search with Qdrant
- ⚡ **Hot Reload** - Instant development feedback

## 🚀 Quick Start

### ⚡ Zero-Setup Demo (30 seconds)
No signups, no API keys, no configuration needed:

```bash
git clone https://github.com/your-username/vibe-stack.git my-app
cd my-app
make dev-demo  # Forces demo mode
```

**Instantly access:**
- **Homepage**: http://localhost:3000 - Beautiful landing page
- **AI Demo**: http://localhost:3000/examples - Working AI integration
- **Backend API**: http://localhost:8000 - Rate-limited FastAPI
- **API Docs**: http://localhost:8000/docs - Auto-generated documentation

### 🔧 Full Setup (5 minutes)
For real projects with database and authentication:

```bash
# 1. Copy environment files
cp .env.example .env
cp .env.example frontend/.env.local

# 2. Add your Supabase keys (see SUPABASE-SETUP.md)
# 3. Start with real services
make dev-real  # Forces real API mode
```

**Quick Setup:** [QUICK-SETUP.md](./QUICK-SETUP.md) | **Detailed Guide:** [SUPABASE-SETUP.md](./SUPABASE-SETUP.md)

## 📚 Documentation

- **[Vibe Stack Guide](./VIBE-STACK-GUIDE.md)** - Complete beginner-friendly walkthrough  
- **[Supabase Setup](./SUPABASE-SETUP.md)** - Database setup options (demo, cloud, local)
- **[New Project Checklist](./NEW-PROJECT-CHECKLIST.md)** - Quick start for new projects
- **[Technical Docs](./CLAUDE.md)** - Detailed architecture and development guide

## 🏗️ Architecture

```
Frontend (Next.js)     Backend (FastAPI)      External Services
     ↓                      ↓                      ↓
┌─────────────┐      ┌─────────────┐         ┌─────────────┐
│  React UI   │ ←──→ │  REST API   │ ←─────→ │  Supabase   │
│  Auth Pages │      │  Auth Logic │         │  (Database) │
│  Dashboard  │      │  AI Routes  │ ←─────→ │  OpenAI     │
└─────────────┘      └─────────────┘         │  Anthropic  │
                                             │   Qdrant    │
                                             └─────────────┘
```

## 🛠️ Available Commands

```bash
# Development Modes
make dev-demo         # Demo mode (no API keys needed)
make dev-real         # Real APIs (requires .env setup)
make dev              # Auto-detect (demo if no keys, real if keys)

# Individual Services  
make dev-frontend     # Frontend only
make dev-backend      # Backend only

# Production
make prod             # Start production environment

# Database
make db-apply         # Apply database migrations
make db-status        # Check migration status

# Utilities
make clean            # Remove containers and volumes
make help             # Show all commands
```

## 🤖 AI Models & Providers

### Supported LLM Models (10 Total)

**OpenAI Models:**
- **o3-pro** - Highest reasoning capability (Premium tier)
- **o3** - Advanced reasoning, cost-efficient (Next tier) 
- **o3-mini** - Fast reasoning model (Next tier)
- **o4-mini** - Fastest, most cost-effective (Budget tier)

**Anthropic Claude Models:**
- **claude-opus-4** - Flagship model, best for deep reasoning (Premium tier)
- **claude-3-5-sonnet** - Balanced performance and cost (Next tier)
- **claude-3-haiku** - Lightweight, fastest Claude model (Budget tier)

**Google Gemini Models:**
- **gemini-2.5-pro** - Deep Think, 1M token context (Premium tier)
- **gemini-2.5-flash** - Fastest Gemini, high-volume efficient (Next tier)
- **gemini-1.5-pro** - Previous generation, affordable (Budget tier)

### Smart Model Selection
- **Task-specific recommendations**: Different models optimized for transcript processing, outline generation, slide generation, reasoning tasks
- **Tier-based pricing**: Budget, next-tier, and premium options for different use cases
- **Automatic fallbacks**: Graceful degradation and error handling
- **Provider status**: Real-time API key validation and provider availability

### API Endpoints
- `/api/models/info` - Complete model information and capabilities
- `/api/models/defaults` - Default model for each provider
- `/api/models/cheapest` - Most cost-effective models
- `/api/llm/generate` - Text generation with any supported model
- `/api/llm/embedding` - Text embeddings
- `/api/llm/demo` - Test AI integration without API keys

## 🔧 Environment Setup

Create environment files:
```bash
cp .env.example .env
cp .env.example frontend/.env.local
```

Required variables:
- `SUPABASE_URL` - Your Supabase project URL
- `SUPABASE_ANON_KEY` - Your Supabase anonymous key  
- `SUPABASE_SERVICE_KEY` - Your Supabase service key

Optional (for AI features):
- `OPENAI_API_KEY` - From [platform.openai.com](https://platform.openai.com)
- `ANTHROPIC_API_KEY` - From [console.anthropic.com](https://console.anthropic.com)
- `GEMINI_API_KEY` - From [aistudio.google.com](https://aistudio.google.com)

## 🎯 What You Get Out of the Box

### Authentication
- ✅ Email/password signup and login
- ✅ OAuth (Google, LinkedIn)
- ✅ Password reset flow
- ✅ Protected routes
- ✅ User session management

### AI Integration
- ✅ **10 LLM Models**: Latest OpenAI (o3-pro, o3, o3-mini, o4-mini), Anthropic Claude (Opus 4, Sonnet 4, Haiku), Google Gemini (2.5 Pro, 2.5 Flash, 1.5 Pro)
- ✅ **Smart Model Selection**: Budget, balanced, and premium tiers with task-specific recommendations
- ✅ **Multi-Provider Support**: Switch between OpenAI, Anthropic, and Google seamlessly
- ✅ **Comprehensive API**: Text generation, embeddings, model comparison, provider status
- ✅ **Demo Mode**: Test AI integration without API keys
- ✅ **Production Ready**: Error handling, rate limiting, authentication, token usage tracking

### Database Features
- ✅ User profiles
- ✅ Row Level Security (RLS)
- ✅ Migration system
- ✅ Real-time subscriptions

### Developer Experience
- ✅ Hot reload for frontend and backend
- ✅ Auto-generated API documentation
- ✅ Type safety (TypeScript + Pydantic)
- ✅ Docker containerization
- ✅ Security headers
- ✅ CORS configuration

## 🚀 Deployment

This template is designed for easy deployment to:
- **Frontend**: Vercel, Netlify
- **Backend**: Railway, Render, Google Cloud Run
- **Database**: Supabase (already hosted)

See deployment guides in the documentation.

## 🤝 Perfect For

- 🧠 **AI-powered applications**
- 📱 **SaaS products**
- 🔐 **Apps requiring authentication**
- ⚡ **Rapid prototyping**
- 🎓 **Learning full-stack development**
- 🤖 **Building with AI assistance (Claude, ChatGPT)**

## 📖 Learning Resources

- [Next.js Documentation](https://nextjs.org/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Supabase Documentation](https://supabase.com/docs)
- [Tailwind CSS](https://tailwindcss.com/)

## 🆘 Getting Help

1. Check the [Vibe Stack Guide](./VIBE-STACK-GUIDE.md) for detailed explanations
2. Use the documentation with AI assistants like Claude or ChatGPT
3. Open an issue for bugs or feature requests

## 📄 License

MIT License - feel free to use this for personal or commercial projects.

---

Built with ❤️ for the vibe coding community