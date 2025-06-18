import { createClient } from '@supabase/supabase-js';

// Initialize the Supabase client
const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL || '';
const supabaseAnonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY || '';

// Check if we're in demo mode
const demoModeEnv = process.env.NEXT_PUBLIC_DEMO_MODE || '';
const isDemoMode = demoModeEnv.toLowerCase() === 'true' || 
                   (!supabaseUrl || !supabaseAnonKey || supabaseUrl === '' || supabaseAnonKey === '');

if (isDemoMode) {
  console.warn('Demo mode active: Supabase client not initialized. Add your keys to enable real authentication.');
}

// Create client only if we have valid credentials, otherwise use a mock
export const supabase = isDemoMode 
  ? null 
  : createClient(supabaseUrl, supabaseAnonKey);

// Demo mode helpers
const DEMO_USER_KEY = 'demo-user-logged-in';

const demoUser = {
  id: 'demo-user-id',
  email: 'demo@vibestack.dev',
  name: 'Demo User'
};

// Demo mode state management
function isDemoLoggedIn() {
  if (typeof window === 'undefined') return false;
  return localStorage.getItem(DEMO_USER_KEY) === 'true';
}

function setDemoLoggedIn(loggedIn: boolean) {
  if (typeof window === 'undefined') return;
  if (loggedIn) {
    localStorage.setItem(DEMO_USER_KEY, 'true');
  } else {
    localStorage.removeItem(DEMO_USER_KEY);
  }
}

// Authentication helpers
export async function signInWithGoogle() {
  if (isDemoMode) {
    setDemoLoggedIn(true);
    return { data: { user: demoUser }, error: null };
  }
  return supabase!.auth.signInWithOAuth({
    provider: 'google',
    options: {
      redirectTo: `${window.location.origin}/auth/callback`,
    },
  });
}

export async function signInWithLinkedIn() {
  if (isDemoMode) {
    setDemoLoggedIn(true);
    return { data: { user: demoUser }, error: null };
  }
  return supabase!.auth.signInWithOAuth({
    provider: 'linkedin',
    options: {
      redirectTo: `${window.location.origin}/auth/callback`,
    },
  });
}

// Email password authentication
export async function signInWithEmail(email: string, password: string) {
  if (isDemoMode) {
    // Simple demo validation
    if (email === 'demo@vibestack.dev' || password.length >= 6) {
      setDemoLoggedIn(true);
      return { data: { user: { ...demoUser, email } }, error: null };
    }
    return { data: null, error: { message: 'Demo mode: Use demo@vibestack.dev or any email with 6+ char password' } };
  }
  return supabase!.auth.signInWithPassword({
    email,
    password,
  });
}

export async function signUpWithEmail(email: string, password: string) {
  if (isDemoMode) {
    if (password.length >= 6) {
      setDemoLoggedIn(true);
      return { data: { user: { ...demoUser, email } }, error: null };
    }
    return { data: null, error: { message: 'Demo mode: Password must be at least 6 characters' } };
  }
  return supabase!.auth.signUp({
    email,
    password,
    options: {
      emailRedirectTo: `${window.location.origin}/auth/callback`,
    },
  });
}

export async function resetPassword(email: string) {
  if (isDemoMode) {
    return { data: {}, error: null };
  }
  return supabase!.auth.resetPasswordForEmail(email, {
    redirectTo: `${window.location.origin}/auth/reset-password`,
  });
}

export async function signOut() {
  if (isDemoMode) {
    setDemoLoggedIn(false);
    return { error: null };
  }
  return supabase!.auth.signOut();
}

export async function getCurrentUser() {
  if (isDemoMode) {
    return isDemoLoggedIn() ? demoUser : null;
  }
  const { data: { user } } = await supabase!.auth.getUser();
  return user;
}

// Session management
export function onAuthStateChange(callback: (event: 'SIGNED_IN' | 'SIGNED_OUT' | 'USER_UPDATED', session: any) => void) {
  if (isDemoMode) {
    // In demo mode, simulate a signed-in state
    setTimeout(() => callback('SIGNED_IN', { user: demoUser }), 100);
    return { data: { subscription: { unsubscribe: () => {} } } };
  }
  return supabase!.auth.onAuthStateChange((event, session) => {
    callback(event as any, session);
  });
}