import tweepy
from dotenv import load_dotenv
import os

#load dotenv to secure API keys
load_dotenv()
api_key=os.getenv("API_KEY")
api_key_secret=os.getenv("API_SECRET")
access_token=os.getenv("ACCESS_TOKEN")
access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")

#authenticate keys
authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticator, wait_on_rate_limit=True)

try:
    api.verify_credentials()
    print("Yup all good boss")
except:
    print("Something broke....")

#Remove "#" from lines to allow for executable code (with this exception of this lime, then stuff breaks)


#Remember to also update keys when changing permissions
#Use this to Follow people, be sure to use the @name, First name, last name does not work
api.create_friendship(screen_name="@elonmusk")

#Use this to auto tweet, add text between the quotes to add your tweet
api.update_status('A bot also wrote this, no I am not hacked, just general screwing around with some Python')

#Use this to update your twitter Description by type your description inside quotes
api.update_profile(description="New Description Here")


#use t#his to get info on a specific user

user = api.get_user("@elonmusk")
print(user.name)
print(user.description)
    #Print Message if this Twitter user hasn't set a description
if user.description=="":
    print("This twitter user did put anything in their description, much empty")
print(user.followers_count)


#Use this to have the bot read your time line and like a specified number of tweets
tweets_home = api.home_timeline(count=10)
for tweet in tweets_home:
    if tweet.author.name.lower() != "@_Xiagax_":
        if not tweet.favorited:
            print(f"Liked {tweet.id ({tweet.author.name})}")
            api.create_favorite(tweet.id)

#Use this to automate liking tweets from a specific user#
user = api.get_user("@elonmusk")

tweets_user = api.user_timeline(user_id=user.id)
for tweet in tweets_user:
    if not tweet.favorited:
        api.create_favorite(tweet.id)
