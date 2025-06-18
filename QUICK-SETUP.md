# ⚡ Quick Setup for Real APIs

## 30-Second Setup

### 1. Create Environment Files
```bash
cp .env.example .env
cp .env.example frontend/.env.local
```

### 2. Get API Keys

#### Supabase (Required - 2 minutes)
1. Go to [supabase.com](https://supabase.com) → "Start your project"
2. Create account → "New Project" → Wait for setup
3. Go to **Settings → API** → Copy these 3 values

#### AI Keys (Optional - 1 minute each)
**OpenAI (ChatGPT):**
1. Go to [platform.openai.com](https://platform.openai.com)
2. Sign up → **API keys** → "Create new secret key"
3. Copy the key: `sk-proj-...`

**Anthropic (Claude):**
1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Sign up → **API Keys** → "Create Key"
3. Copy the key: `sk-ant-...`

### 3. Add Keys to Both Files
**Edit `.env` AND `frontend/.env.local`:**

```bash
# Replace with YOUR values from Supabase:
SUPABASE_URL=https://xxxxx.supabase.co
SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI...
SUPABASE_SERVICE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI...

# Optional (for AI features):
OPENAI_API_KEY=sk-your-key
ANTHROPIC_API_KEY=sk-ant-your-key
```

### 4. Start with Real APIs
```bash
make dev-real
```

## ✅ Done!
- Real user authentication ✅
- Real database ✅
- Real AI (if keys added) ✅
- Visit: http://localhost:3000

## 💰 API Key Costs
- **Supabase**: Free tier (500MB database, 50MB storage)
- **OpenAI**: Pay-per-use (~$0.002 per request)
- **Anthropic**: Pay-per-use (~$0.003 per request)

*All have free credits for new users!*

---

**Need help?** See [SUPABASE-SETUP.md](./SUPABASE-SETUP.md) for detailed steps.