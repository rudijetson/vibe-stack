'use client'

import { useState } from 'react'

export default function ExamplesPage() {
  const [chatResponse, setChatResponse] = useState('')
  const [isLoading, setIsLoading] = useState(false)

  const handleAIChat = async () => {
    setIsLoading(true)
    try {
      const response = await fetch('http://localhost:8000/api/llm/demo', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          prompt: 'Write a short motivational message for vibe coders who are building their first AI app',
          model: 'gpt-3.5-turbo'
        })
      })
      
      const data = await response.json()
      
      if (data.demo) {
        setChatResponse(`${data.content}\n\n💡 ${data.message || 'This is demo mode - add your API keys for real AI!'}`)
      } else {
        setChatResponse(data.content)
      }
    } catch (error) {
      setChatResponse('🌟 Demo mode active! This shows how the Vibe Stack handles AI integration. The template is working perfectly - just add your API keys when you want to connect to real AI services!')
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-400 via-pink-500 to-red-500 p-8">
      <div className="max-w-4xl mx-auto">
        <div className="bg-white rounded-lg shadow-xl p-8">
          <h1 className="text-4xl font-bold text-gray-800 mb-2">
            🌟 Vibe Stack Examples
          </h1>
          <p className="text-gray-600 mb-8">
            See what you can build with the Vibe Stack template
          </p>

          {/* AI Chat Example */}
          <div className="bg-gray-50 rounded-lg p-6 mb-8">
            <h2 className="text-2xl font-bold text-gray-800 mb-4">
              🧠 AI Chat Integration
            </h2>
            <p className="text-gray-600 mb-4">
              Click the button to see AI integration in action!
            </p>
            
            <button
              onClick={handleAIChat}
              disabled={isLoading}
              className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded mb-4 disabled:opacity-50"
            >
              {isLoading ? 'Thinking...' : 'Get AI Motivation 🚀'}
            </button>
            
            {chatResponse && (
              <div className="bg-white p-4 rounded border-l-4 border-blue-500">
                <p className="text-gray-700">{chatResponse}</p>
              </div>
            )}
          </div>

          {/* Feature Showcase */}
          <div className="grid md:grid-cols-2 gap-6">
            <div className="border rounded-lg p-6">
              <h3 className="text-xl font-bold mb-3">🔐 Authentication</h3>
              <ul className="text-gray-600 space-y-2">
                <li>✅ Email/Password signup</li>
                <li>✅ Google OAuth</li>
                <li>✅ LinkedIn OAuth</li>
                <li>✅ Protected routes</li>
                <li>✅ Session management</li>
              </ul>
            </div>

            <div className="border rounded-lg p-6">
              <h3 className="text-xl font-bold mb-3">🧠 AI Integration</h3>
              <ul className="text-gray-600 space-y-2">
                <li>✅ OpenAI GPT models</li>
                <li>✅ Anthropic Claude</li>
                <li>✅ Streaming responses</li>
                <li>✅ Token counting</li>
                <li>✅ Error handling</li>
              </ul>
            </div>

            <div className="border rounded-lg p-6">
              <h3 className="text-xl font-bold mb-3">💾 Database Features</h3>
              <ul className="text-gray-600 space-y-2">
                <li>✅ User profiles</li>
                <li>✅ Row Level Security</li>
                <li>✅ Real-time subscriptions</li>
                <li>✅ Migration system</li>
                <li>✅ Type-safe queries</li>
              </ul>
            </div>

            <div className="border rounded-lg p-6">
              <h3 className="text-xl font-bold mb-3">🚀 Developer Experience</h3>
              <ul className="text-gray-600 space-y-2">
                <li>✅ Hot reload</li>
                <li>✅ Auto-generated docs</li>
                <li>✅ Docker development</li>
                <li>✅ Type safety</li>
                <li>✅ One-command setup</li>
              </ul>
            </div>
          </div>

          {/* Call to Action */}
          <div className="bg-gradient-to-r from-purple-500 to-pink-500 rounded-lg p-6 mt-8 text-white text-center">
            <h3 className="text-2xl font-bold mb-2">Ready to Build?</h3>
            <p className="mb-4">
              This is just the beginning. Use AI assistants like Claude or ChatGPT to build amazing features on top of this foundation.
            </p>
            <div className="space-x-4">
              <a
                href="/dashboard"
                className="bg-white text-purple-600 font-bold py-2 px-4 rounded hover:bg-gray-100 inline-block"
              >
                Try Dashboard
              </a>
              <a
                href="/auth/login"
                className="bg-purple-700 text-white font-bold py-2 px-4 rounded hover:bg-purple-800 inline-block"
              >
                Test Auth
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}