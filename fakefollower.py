import tweepy
import time
from datetime import datetime
import keys
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')

auth=tweepy.OAuthHandler(keys.consumer_key,keys.consumer_secret)
auth.set_access_token(keys.access_token,keys.access_token_secret)
api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)


def follower_following(username):
    user=api.get_user(username)
    followers=user.followers_count
    following=user.friends_count
    ratio=followers*50//following
    if ratio > 1:
        print("GREEN")

def facedetection(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.03, 5)
    if len(faces)>=1:
        return True
    else:
        return False

def profilephoto(username):
    user=api.get_user(username)
    response = requests.get(user.profile_image_url)
    img = Image.open(BytesIO(response.content))
    image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    image = cv2.resize(image, (400, 700)) 
    val=facedetection(image)
    if(val):
        print("GREEN")
    else:
        print("RED")

def bannerphoto(username):
    user=api.get_user(username)
    response = requests.get(user.profile_banner_url)
    img = Image.open(BytesIO(response.content))
    image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    image = cv2.resize(image, (400, 700)) 
    val=facedetection(image)
    if(val):
        print("GREEN")
    else:
        print("RED")

def regularity(username):
    now=datetime.now()
    user=api.get_user(username)
    status=api.user_timeline(user.id)
    dates_tweet=list()
    dates_retweet=list()
    for i in status:
        if 'RT' not in i.text:
            dates_tweet.append(i.created_at)
        else:
            dates_retweet.append(i.created_at)

    if(len(dates_tweet)!=0):
        mean_tweet = (np.array(dates_tweet, dtype='datetime64[s]')
        .view('i8')
        .mean()
        .astype('datetime64[s]'))
        mean_tweet=datetime.strptime(str(mean_tweet),'%Y-%m-%dT%H:%M:%S')
        print(now-mean_tweet)
    if(len(dates_retweet)!=0):
        mean_retweet = (np.array(dates_retweet, dtype='datetime64[s]')
        .view('i8')
        .mean()
        .astype('datetime64[s]'))
        mean_retweet=datetime.strptime(str(mean_retweet),'%Y-%m-%dT%H:%M:%S')
        print(now-mean_retweet)

def source(username):
    user=api.get_user(username)
    status=api.user_timeline(user.id)
    if status[0].source=='twitter bot autotweet':
        print("Confirm bot")
        quit()

    

name=input("ENTER USERNAME:")
try:
    api.verify_credentials()
except:
    print("Some problem occured")
    quit()
try:
    api.get_user(name)
except:
    print("User not found")
    quit()

source(name)
follower_following(name)

try:
    profilephoto(name)
except:
    print("RED")
try:
    bannerphoto(name)
except:
    print("RED")
regularity(name)
