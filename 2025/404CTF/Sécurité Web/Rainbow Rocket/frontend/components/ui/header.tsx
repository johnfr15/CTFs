import { useState, useEffect } from 'react';
import Link from 'next/link';
import MobileMenu from './mobile-menu';
import Image from 'next/image';
import Cookies from 'js-cookie';
import axios from 'axios';
import React from 'react';
require('dotenv').config();
axios.defaults.baseURL = process.env.NEXT_PUBLIC_BACKEND_URL;
export default function Header() {
  const [balance, setBalance] = useState<string | null>(null);
  const [user, setUser] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(true); 

  useEffect(() => {
    const userCookie = Cookies.get('token');
    if (userCookie) {
      axios.post('/verification', { token: userCookie })
        .then(response => {
          setIsLoading(false); 
          if (response.status === 200) {
            const username  = (response.data as { message: string }).message;
            setUser(username);
          } else {
            setIsLoading(false); 

            setUser('Unauthorized');
          }
        })
        .catch(err => {
          setIsLoading(false); 

          setUser('Unauthorized');
        });
    }
    setIsLoading(false); 
  }, []);
  if (isLoading) {
    return <div>          <MobileMenu />
    </div>;
  }
  return (
    <header className="absolute w-full z-30">
      <div className="max-w-6xl mx-auto px-4 sm:px-6">
        <div className="flex justify-between items-center h-20">
          {/* Site branding */}
          <div className="shrink-0 mr-4">
            {/* Logo */}
            <Link href="/" className="block" aria-label="Cruip">
            </Link>
          </div>

          {/* Desktop navigation */}
          <nav className="hidden md:flex md:items-center md:justify-end flex-grow">
            {/* Desktop sign in links */}
            { user ? (
              <div className="flex items-center">
                <ul className="flex space-x-4">
                  <li>
                  <a
                    onClick={() => {
                      Cookies.remove("token");
                      Cookies.remove("balance");
                      window.location.href = "/";
                    }}
                    className="font-medium text-red-600 hover:text-gray-200 px-4 py-3 flex items-center transition duration-150 ease-in-out"
                    href="#"
                  >
                    Déconnexion
                  </a>
                  </li>
                  <li>
                
                  </li>
                </ul>
              </div>
            ) : (
              <ul className="flex space-x-4">
                <li>
                  <Link
                    href="/login/index.html"
                    className="font-medium text-purple-600 hover:text-gray-200 px-4 py-3 flex items-center transition duration-150 ease-in-out"
                  >
                    Connexion
                  </Link>
                </li>
                <li>
                  <Link href="/register/index.html" className="btn-sm text-white bg-purple-600 hover:bg-purple-700">
                    Inscription
                  </Link>
                </li>
              </ul>
            )}
          </nav>

          <MobileMenu />

        </div>
      </div>
    </header>
  );
}
