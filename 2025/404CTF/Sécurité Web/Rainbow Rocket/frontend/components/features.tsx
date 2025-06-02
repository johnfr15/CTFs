'use client'
import Image from 'next/image'
import axios from 'axios';
import { useState, useEffect } from 'react';
import React from 'react';
import '../public/notification.css';
import MyNotification from '../public/notification.js'; 
require('dotenv').config();
axios.defaults.baseURL = process.env.BACKEND_URL;

export default function Features() {
  useEffect(() => {
    const urlParams = new URLSearchParams(window.location.search);
    const reponse = urlParams.get('reponse');
    if (reponse === '4') {
      console.log('Vous devez être connecté(e) pour acheter un billet');
      const popup =  MyNotification({
        position: 'bottom-right',
        duration: 7000
      });
      popup.error({
        title: 'Erreur',
        message: 'Vous devez être connecté(e) pour acheter un billet'
      });
    } else if (reponse === '3') {
      const popup = MyNotification({
        position: 'bottom-right',
        duration: 7000
      });
      popup.error({
        title: 'Erreur',
        message: 'Hacker Détecté'
      });
    } else if (reponse === '2') {
      const popup = MyNotification({
        position: 'bottom-right',
        duration: 7000
      });
      popup.error({
        title: 'Erreur',
        message: 'Solde insuffisant'
      });
    } else if (reponse === '1') {
      const popup = MyNotification({
        position: 'bottom-right',
        duration: 7000
      });
      popup.info({
        title: 'Merci pour votre achat',
        message: 'Vous pouvez consulter vos billets dans l\'onglet Mes billets'
      });
    }
  }, []);

  return (
    <div> </div>
      )
}
