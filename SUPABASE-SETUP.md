# 🗄️ Supabase Setup Guide

This guide helps you set up Supabase for your Vibe Stack project. Choose your path:

## 🚀 Quick Start Paths

### Option 1: Demo Mode (Instant) ⚡
**Perfect for**: First-time exploration, testing the template

```bash
make dev-demo
# Visit http://localhost:3000/examples
```

**What you get:**
- ✅ Working AI demo (mock responses)  
- ✅ Full UI experience
- ✅ No signups required
- ❌ No real database
- ❌ No real authentication

---

### Option 2: Free Supabase Cloud (5 minutes) ☁️
**Perfect for**: Real projects, prototypes, MVP development

#### Step 1: Create Supabase Account
1. Go to [supabase.com](https://supabase.com)
2. Click "Start your project"
3. Sign up with GitHub (recommended)

#### Step 2: Create Project
1. Click "New Project"
2. Choose organization (personal)
3. Set project name: `my-vibe-stack-app`
4. Set database password (save this!)
5. Choose region (closest to you)
6. Click "Create new project"

#### Step 3: Get Your Keys
1. Go to Settings → API
2. Copy these values:
   - **Project URL**: `https://xxxxx.supabase.co`
   - **anon key**: `eyJhbGciOiJIUzI1NiIsInR5cCI...`
   - **service_role key**: `eyJhbGciOiJIUzI1NiIsInR5cCI...`

#### Step 4: Add Keys to Your Project
```bash
# Copy environment files
cp .env.example .env
cp .env.example frontend/.env.local

# Edit both files and add your Supabase values:
# SUPABASE_URL=https://xxxxx.supabase.co
# SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI...
# SUPABASE_SERVICE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI...
```

#### Step 5: Start Your App
```bash
make dev
```

**What you get:**
- ✅ Real database (PostgreSQL)
- ✅ Real authentication
- ✅ User management
- ✅ 500MB database
- ✅ 50MB file storage
- ✅ Row Level Security

---

### Option 3: Local Supabase (Advanced) 🏠
**Perfect for**: Offline development, team environments

*Coming soon in next update!*

---

## 🎯 What's Next?

### After Setup:
1. **Visit**: http://localhost:3000
2. **Try login**: Create account or sign in
3. **Test dashboard**: Protected routes work
4. **Add AI keys**: Optional OpenAI/Anthropic integration

### Add AI Services (Optional):

#### OpenAI (ChatGPT) Setup:
1. Go to [platform.openai.com](https://platform.openai.com)
2. Sign up or log in
3. Click **API keys** in the left sidebar
4. Click **"Create new secret key"**
5. Copy the key (starts with `sk-proj-` or `sk-`)
6. Add to both `.env` files: `OPENAI_API_KEY=sk-your-key`

#### Anthropic (Claude) Setup:
1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Sign up or log in  
3. Click **API Keys** in the left sidebar
4. Click **"Create Key"**
5. Copy the key (starts with `sk-ant-`)
6. Add to both `.env` files: `ANTHROPIC_API_KEY=sk-ant-your-key`

```bash
# Your .env files should look like:
OPENAI_API_KEY=sk-proj-your-actual-key-here
ANTHROPIC_API_KEY=sk-ant-your-actual-key-here
```

### Database Management:
- **Supabase Dashboard**: Your project URL + `/dashboard`
- **SQL Editor**: Write custom queries
- **Table Editor**: Visual table management
- **Authentication**: User management

---

## 🆘 Troubleshooting

### "SUPABASE_URL not set" warnings
- Make sure you created the `.env` files
- Check the values are correct (no quotes needed)
- Restart containers: `make clean && make dev`

### Authentication errors
- Verify your anon key is correct
- Check CORS settings in Supabase dashboard
- Make sure site URL is set to `http://localhost:3000`

### Database connection issues
- Verify service_role key is correct
- Check if your project is paused (free tier auto-pauses)
- Restart project in Supabase dashboard

---

## 🎉 Pro Tips

1. **Bookmark your Supabase dashboard** - you'll use it often
2. **Enable database backups** - Settings → Database → Backups  
3. **Set up GitHub integration** - for automatic migrations
4. **Monitor usage** - free tier has limits but they're generous
5. **Join Supabase Discord** - amazing community support

---

## 🔄 Migration from Demo Mode

Already using demo mode? Easy upgrade:

1. Follow "Option 2" above to get Supabase keys
2. Add keys to your `.env` files  
3. Restart: `make clean && make dev`
4. Your data will automatically sync to real database!

---

Ready to build something amazing? Your database is waiting! 🚀