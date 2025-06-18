import { useState, useEffect } from 'react';

const DEMO_USER_KEY = 'demo-user-logged-in';

export function useDemoAuth() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    // Check if user is logged in demo mode
    const demoLoggedIn = localStorage.getItem(DEMO_USER_KEY) === 'true';
    setIsLoggedIn(demoLoggedIn);
  }, []);

  const demoSignIn = () => {
    localStorage.setItem(DEMO_USER_KEY, 'true');
    setIsLoggedIn(true);
  };

  const demoSignOut = () => {
    localStorage.removeItem(DEMO_USER_KEY);
    setIsLoggedIn(false);
  };

  return {
    isLoggedIn,
    demoSignIn,
    demoSignOut
  };
}