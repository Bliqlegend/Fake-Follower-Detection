import tweepy
import time
import keys
auth=tweepy.OAuthHandler(keys.consumer_key,keys.consumer_secret)
auth.set_access_token(keys.access_token,keys.access_token_secret)
api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
def follower_following(username):
    user=api.get_user(username)
    followers=user.followers_count
    following=user.friends_count
    ratio=followers*50//following
    if ratio > 1:
        print("green")


def profilephoto(username):
    user=api.get_user(username)
    print(user.profile_image_url)

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

follower_following(name)
profilephoto(name)
