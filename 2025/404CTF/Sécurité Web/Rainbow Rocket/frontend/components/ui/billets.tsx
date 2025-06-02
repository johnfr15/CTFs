import { useState, useEffect } from 'react';
import MobileMenu from './mobile-menu';
import Cookies from 'js-cookie';
import axios from 'axios';
import React from 'react';
require('dotenv').config();
axios.defaults.baseURL = process.env.BACKEND_URL;

export default function Billets() {
  const [billets, setBillets] = useState<any | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(true); 

  useEffect(() => {
    const userCookie = Cookies.get('token');
    if (userCookie) {
      axios.post('/billets', { token: userCookie })
        .then(response => {
          setIsLoading(false); 
          if (response.status === 200) {
            const billets = (response.data as { message: any }).message;
            setBillets(billets);
          } else {
            setIsLoading(false); 

            setBillets('Unauthorized');
          }
        })
        .catch(err => {
          setIsLoading(false); 

          setBillets('Unauthorized');
        });
    } else {
      setIsLoading(false); 
    }
  }, []);
  if (isLoading) {
    return <div><MobileMenu /></div>; 
  }
  return (
    <>
      {billets !== 'Unauthorized' ? (
        Object.entries(billets).map(([key, value], index) => (
          <div key={index} className="relative flex flex-col items-center m-4" data-aos="fade-up">
            <h4 className="h4 mb-2">{key}</h4>
            <p className="text-lg text-gray-400 text-center">You have {value as number} ticket(s) in this category.</p>
          </div>
        ))
      ) : (
        <div>
          <h1>Unauthorized</h1>
        </div>
      )}
    </>
  );
}