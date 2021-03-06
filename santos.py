import os
import tweepy
import time
import datetime
from os import environ

CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_KEY = os.environ.get('ACCESS_KEY')
ACCESS_SECRET = os.environ.get('ACCESS_SECRET')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
print(api.me())               

if __name__ == "__main__":
    while True:
        class MyStreamListener(tweepy.StreamListener):
            def on_status(self, status):
                if status.user.screen_name == "SantosFC" and not "RT" in status.text:
                     try:
                         api.create_favorite(status.id)
                         print(status.text)
                     except tweepy.TweepError as e:
                         print(e.reason)
                else:
                    print("n")  
                                                      
        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
        myStream.filter(follow=["49751816"])

