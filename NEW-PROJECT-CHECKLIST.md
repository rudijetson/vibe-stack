# 🚀 New Project Quick Start Checklist

Use this checklist every time you start a new project with the Vibe Stack.

## 1️⃣ Copy the Template
```bash
# If using GitHub template
# Click "Use this template" on GitHub

# If using local copy
cp -r path/to/vibe-stack-template my-new-project
cd my-new-project
```

## 2️⃣ Initialize Git
```bash
rm -rf .git              # Remove template's git history
git init                 # Start fresh
git add .
git commit -m "Initial commit from Vibe Stack"
```

## 3️⃣ Set Up Environment
```bash
# Run the setup script
./first-time.sh

# Or manually copy env files
cp .env.example .env
cp .env.example frontend/.env.local
```

## 4️⃣ Configure Your Project

### Update Project Name
1. Edit `frontend/package.json`:
   - Change `"name": "your-project-name"`
   - Update `"description"`

2. Edit `frontend/app/layout.tsx`:
   - Update `<title>Your App Name</title>`
   - Update metadata

### Set Up Supabase
1. Create new project at [supabase.com](https://supabase.com)
2. Get your project URL and keys
3. Add to both `.env` files:
   ```
   SUPABASE_URL=your-project-url
   SUPABASE_ANON_KEY=your-anon-key
   SUPABASE_SERVICE_KEY=your-service-key
   ```

### Optional: AI Services
If using AI features, add keys:
```
OPENAI_API_KEY=your-key
ANTHROPIC_API_KEY=your-key
```

## 5️⃣ Customize Basics

### Brand Colors
Edit `frontend/tailwind.config.js`:
```js
colors: {
  primary: '#your-color',
  secondary: '#your-color',
}
```

### Homepage
Edit `frontend/app/page.tsx`:
- Update hero text
- Change call-to-action
- Modify description

### Login Page
Edit `frontend/app/auth/login/page.tsx`:
- Update branding
- Customize welcome message

## 6️⃣ Start Development
```bash
make dev
```
- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- API Docs: http://localhost:8000/docs

## 7️⃣ Test Everything
- [ ] Homepage loads
- [ ] Can navigate to /auth/login
- [ ] Can sign up for account
- [ ] Can log in
- [ ] Dashboard shows after login
- [ ] API docs load at :8000/docs

## 8️⃣ First Feature Checklist
When adding your first feature:
- [ ] Plan the UI (what users see)
- [ ] Plan the API (what data moves)
- [ ] Copy similar existing patterns
- [ ] Test locally
- [ ] Commit changes

## 9️⃣ Deployment Prep
- [ ] Update `CORS_ORIGINS` in `.env` with your domain
- [ ] Set production environment variables
- [ ] Test with `make prod` locally
- [ ] Push to GitHub
- [ ] Deploy!

## 🎯 Common First Features

### Add a New Page
1. Create folder: `frontend/app/features/`
2. Add `page.tsx`
3. Copy pattern from existing page

### Add Database Table
1. Create: `supabase/migrations/002_your_table.sql`
2. Define schema
3. Run: `make db-apply`

### Add API Endpoint
1. Create: `backend/app/api/endpoints/your_feature.py`
2. Copy pattern from `llm.py`
3. Add router to `main.py`

## 💡 Pro Tips
- Keep this template clean - don't add project-specific code
- Update the template when you find better patterns
- Each project gets its own Supabase project
- Use different git repos for each project

---

Ready to build something awesome? Let's go! 🚀