import tweepy
import time
from datetime import datetime
import keys
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import cv2
from termcolor import cprint,colored

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')

auth=tweepy.OAuthHandler(keys.consumer_key,keys.consumer_secret)
auth.set_access_token(keys.access_token,keys.access_token_secret)
api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

univ_flag = 0

def url_linked(username):
    l_url = []
    user = api.get_user(username)
    url_user = user.url
    r = requests.get(url_user) 
    ele = r.url
    l_url.append(ele)
    cprint("[+]",'cyan')
    cprint("Found Url's",'green')
    for i in l_url:
      cprint("[*]",'yellow')
      cprint(i,'cyan')

def follower_following(username):
    user=api.get_user(username)
    followers=user.followers_count
    following=user.friends_count
    ratio=followers*50//following
    if ratio > 1:
        cprint("[+]",'magenta')
        cprint("Profile Photo seems Legit",'green')

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
        cprint("[+]",'magenta')
        cprint("Profile Photo seems Legit",'green')
    else:
        cprint("[-]",'cyan')
        cprint("Profile Photo Doesn't seem legit",'red')
        univ_flag+=1

def bannerphoto(username):
    user=api.get_user(username)
    response = requests.get(user.profile_banner_url)
    img = Image.open(BytesIO(response.content))
    image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    image = cv2.resize(image, (400, 700)) 
    val=facedetection(image)
    if(val):
        cprint("[+]",'magenta')
        cprint("Banner Photo seems Legit",'green')
    else:
        cprint("[-]",'cyan')
        cprint("Banner Photo Doesn't seem legit",'red')
        univ_flag+=1
        

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
        cprint('[*]','cyan')
        cprint('Frequency of tweets :','yellow')
        print(now-mean_tweet)
    if(len(dates_retweet)!=0):
        mean_retweet = (np.array(dates_retweet, dtype='datetime64[s]')
        .view('i8')
        .mean()
        .astype('datetime64[s]'))
        mean_retweet=datetime.strptime(str(mean_retweet),'%Y-%m-%dT%H:%M:%S')
        cprint('[*]','cyan')
        cprint('Frequency of retweets :','yellow')
        print(now-mean_retweet)

def source(username):
    user=api.get_user(username)
    status=api.user_timeline(user.id)
    if status[0].source=='twitter bot autotweet':
        cprint("[-] Account is a Confirmed bot",'red')
        quit()


def likes_freq(username):
    user = api.get_user(username)
    fav = user.favourites_count 
    time = user.created_at
    cprint(f"Account Created {time.day}th of {time.month} in {time.year}",'green')
    rn  = datetime.now()
    deff = rn - time
    total_days = deff.days
    check_flag = 1
    if fav <= total_days/total_days:
        check_flag = 0
        cprint("[-]",'cyan')
        cprint("Likes rate is too low",'red')
    if fav == total_days:
        check_flag = 1
    if fav > 50*total_days:
        check_flag = 0
        cprint("[-]",'cyan')
        cprint("Likes rate is too high",'red')

    if check_flag == 1:
        cprint("[+]",'magenta')
        cprint("Likes Seem to be in Order",'green')
    else:
        cprint("[-]",'cyan')
        cprint("Likes Don't Seem to be in Order",'red')
        univ_flag+=1

#main
cprint("Enter the Username to test : ",'yellow')
name= input()
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
#follower_following

follower_following(name)

try:
#photo
    profilephoto(name)
except:
    cprint("[-]",'cyan')
    cprint("Profile Picture Doesn't seem legit",'red')
    univ_flag+=1


try:
#Banner Photo
    bannerphoto(name)
except:
    cprint("[-]",'cyan')
    cprint("Banner Photo Doesn't seem legit",'red')
    univ_flag+=1

#regularity
regularity(name)

#url_linked
try:
  url_linked(name)
except:
    cprint("[-]",'cyan')
    cprint("User Doesn't Seem to contain any Url's",'red')

likes_freq(name)

cprint(f'This Account got {univ_flag} red flag','red')