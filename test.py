import keys
import tweepy
import re
import requests

# Authenticate to Twitter
auth=tweepy.OAuthHandler(keys.consumer_key,keys.consumer_secret)
auth.set_access_token(keys.access_token,keys.access_token_secret)
api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

username = input("Username  > ")

user = api.get_user(username)

print("User details:")
print(user.name)
print(user.description)
print(user.location)
url_user = user.url
print(f"URL : {url_user}")
r = requests.get(url_user) 
print(r.url)
# url_reggex = re.compile(r'(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)')
# check_var = url_reggex.search(descrip)
# print("Url : "+ check_var.group(1) )
# print("Last 20 Followers:")
# for follower in user.followers():
#     print(follower.name)

