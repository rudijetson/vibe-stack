import Link from 'next/link';

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen p-4">
      <div className="max-w-4xl mx-auto text-center">
        <h1 className="text-4xl font-bold tracking-tight text-gray-900 sm:text-5xl md:text-6xl">
          <span className="block">🌟 The Vibe Stack</span>
          <span className="block text-purple-600">AI-First Full-Stack Template</span>
        </h1>

        <p className="mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg max-w-xl mx-auto">
          Build AI-powered web apps in minutes, not weeks. Perfect for vibe coders who use Claude, ChatGPT, and Cursor to ship fast.
        </p>

        <div className="mt-8 sm:mt-12">
          <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 md:grid-cols-3">
            <FeatureCard
              title="FastAPI Backend"
              description="High-performance API with Python FastAPI"
              icon="🚀"
            />
            <FeatureCard
              title="Next.js Frontend"
              description="React framework with SSR and routing"
              icon="⚛️"
            />
            <FeatureCard
              title="Supabase Integration"
              description="Authentication, database, and storage"
              icon="🔐"
            />
            <FeatureCard
              title="LLM Ready"
              description="OpenAI and Claude API integrations"
              icon="🤖"
            />
            <FeatureCard
              title="Tailwind CSS"
              description="Utility-first CSS framework"
              icon="🎨"
            />
            <FeatureCard
              title="Docker Ready"
              description="Development and production containers"
              icon="🐳"
            />
          </div>
        </div>

        <div className="mt-8 sm:mt-12 space-y-4">
          <div className="space-x-4">
            <Link href="/examples" className="bg-purple-600 hover:bg-purple-700 text-white font-bold py-3 px-6 rounded-lg inline-block">
              🚀 See Examples
            </Link>
            <Link href="/dashboard" className="bg-gray-600 hover:bg-gray-700 text-white font-bold py-3 px-6 rounded-lg inline-block">
              Try Dashboard
            </Link>
          </div>
          <p className="text-sm text-gray-500">
            ⚡ Ready to deploy • 🧠 AI-integrated • 🔐 Auth included • 🐳 Docker ready
          </p>
        </div>
      </div>
    </div>
  );
}

function FeatureCard({ title, description, icon }: { title: string; description: string; icon: string }) {
  return (
    <div className="flex flex-col p-6 bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow">
      <div className="flex items-center">
        <span className="text-3xl mr-3">{icon}</span>
        <h3 className="text-lg font-medium text-gray-900">{title}</h3>
      </div>
      <p className="mt-2 text-sm text-gray-500">{description}</p>
    </div>
  );
}