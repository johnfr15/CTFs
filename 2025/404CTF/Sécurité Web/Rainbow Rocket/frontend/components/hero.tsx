"use client";
import React, { useEffect, useState } from "react";
import Cookies from "js-cookie";
import axios from "axios";
require('dotenv').config(); 


axios.defaults.baseURL = process.env.BACKEND_URL;

export default function Hero() {
  const [flag, setFlag] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(true);

  useEffect(() => {
    const token = Cookies.get("token");

    const fetchFlag = async () => {
      try {
        const response = await axios.get<{ flag: string }>("/flag", {
          headers: { Authorization: `Bearer ${token}` }, 
        });
        setFlag(response.data.flag);
      } catch (error) {
        setFlag(null); 
      } finally {
        setIsLoading(false);
      }
    };

    if (token) {
      fetchFlag();
    } else {
      setIsLoading(false);
    }
  }, []);

  return (
    <div className="flex flex-col items-center justify-center min-h-screen">
      {isLoading ? (
        <p className="text-2xl">Loading...</p>
      ) : flag ? (
        <>
          <h1 className="text-4xl font-bold mb-4">Good job!</h1>
          <p className="text-2xl text-green-500">{flag}</p>
        </>
      ) : (
        <h1 className="text-3xl text-red-500">Vous devez être admin pour voir cette page</h1>
      )}
    </div>
  );
}
