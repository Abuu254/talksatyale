"use client";

import styles from '../page.module.css'
import React, { useState, useEffect, use } from 'react'
import axios from 'axios'
import FriendModal from './friendModal';

const API_ENDPOINT = 'http://localhost:8080';  // constant url, used to fetch data from backend

export default function FriendSection() {

  const [friends, setFriends] = useState(null);
  const [refresh, setRefresh] = useState(false);

  useEffect(() => { async function getFriends () {

    try {
      const headers = new Headers();
      console.log("Getting friends");
      const accessToken = localStorage.getItem('access_token');
      console.log('Access token:', accessToken);
      if (accessToken) {
        headers.append('Authorization', `Bearer ${accessToken}`);
      }
      const url = API_ENDPOINT + '/list_friends';
      const response = await fetch(url,{
      credentials: 'include',
      headers: headers,
    });
      const data = await response.json();
      setFriends(data);
      console.log("Friends: ", data);
    }

    catch (error) {
      console.error("Error finding friends:", error);
    }
  }
  getFriends();
}, [refresh]);

    const [isShown, setIsShown] = useState(false);


    const openFriend = event => {

      try {
          setIsShown(true);
          console.log("Manage friend clicked!");
        } catch (error) {
          console.error('Error when card clicked:', error);
        }

    };
    const closeModal = () => {
        setIsShown(false);
        setRefresh(!refresh);
      };

      function FriendImage({ src, alt }) {
        const [imgSrc, setImgSrc] = useState(src);

        useEffect(() => {
          const img = new window.Image();
          img.src = src;
          img.onload = () => setImgSrc(src);
          img.onerror = () => setImgSrc("https://static.vecteezy.com/system/resources/thumbnails/005/544/718/small/profile-icon-design-free-vector.jpg");
        }, [src]);

        return <img className={styles.friendImages} src={imgSrc} alt={alt} />;
      }

    return (
      <div className={styles.friendSection}>
        {isShown && (
        <FriendModal onClose={closeModal}/>
            )}
        <div className={styles.myFriends}>
          {friends?.map(friend => (
            <a href={`http://localhost:3000/user?net_id=${friend.netid}`} key={friend.netid}>
              <FriendImage src={friend.photo_link} alt={friend.netid} />
            </a>
          ))}
        </div>
        <button className={styles.friendButton} onClick={openFriend}>
            <h2>Manage Friends</h2>
        </button>


      </div>

    )
  }
