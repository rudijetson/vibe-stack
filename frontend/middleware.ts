import { createServerClient } from '@supabase/ssr'
import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

export async function middleware(req: NextRequest) {
  const res = NextResponse.next()
  
  // Check if we have Supabase credentials
  const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL
  const supabaseAnonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY
  const demoModeEnv = process.env.NEXT_PUBLIC_DEMO_MODE || ''
  
  // In demo mode, allow access to everything except auth routes
  const isDemoMode = demoModeEnv.toLowerCase() === 'true' || 
                     !supabaseUrl || !supabaseAnonKey || supabaseUrl === '' || supabaseAnonKey === ''
  
  if (isDemoMode) {
    // In demo mode, redirect auth routes to dashboard (since auth doesn't work)
    if (req.nextUrl.pathname.startsWith('/auth')) {
      return NextResponse.redirect(new URL('/dashboard', req.url))
    }
    
    // Allow everything else in demo mode
    return res
  }
  
  // Real Supabase mode - use proper authentication
  try {
    const supabase = createServerClient(
      supabaseUrl,
      supabaseAnonKey,
      {
        cookies: {
          get(name: string) {
            return req.cookies.get(name)?.value
          },
          set(name: string, value: string, options: any) {
            res.cookies.set({ name, value, ...options })
          },
          remove(name: string, options: any) {
            res.cookies.set({ name, value: '', ...options })
          },
        },
      }
    )
    
    const { data: { session } } = await supabase.auth.getSession()

    // Protect dashboard routes
    if (req.nextUrl.pathname.startsWith('/dashboard')) {
      if (!session) {
        return NextResponse.redirect(new URL('/', req.url))
      }
    }

    // Redirect authenticated users away from auth pages
    if (req.nextUrl.pathname.startsWith('/auth') && session) {
      return NextResponse.redirect(new URL('/dashboard', req.url))
    }
  } catch (error) {
    // If there's an error with Supabase, fall back to demo mode behavior
    console.warn('Supabase middleware error, falling back to demo mode:', error)
    
    if (req.nextUrl.pathname.startsWith('/auth')) {
      return NextResponse.redirect(new URL('/dashboard', req.url))
    }
  }

  return res
}

export const config = {
  matcher: ['/dashboard/:path*', '/auth/:path*']
}