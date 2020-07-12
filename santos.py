import tweepy
import time

auth = tweepy.OAuthHandler('3aRyfr1fD2ybyyRcgb7mFg3R5', 'maed6uLK7e8BdZHTGZsR5iiSDuaESsuRZLzE4g8jGp2ukYycKv')
auth.set_access_token('2186612092-2vFsuN7Q5YLxzUJP5XMIavPrYryseDexCPVGkLt', 'Yo7GqeEuacHiNXuB8mTWM3eLVrTvfUnF0QOlxLlSimCMv')
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()
print(user)

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
                if status.user.screen_name == "SantosFC" and not "RT" in status.text:
                    print(status.text)
                    try:                     
                     api.create_favorite(status.id)
                     # api.retweet(status.id)
                    except tweepy.TweepError as e:
                     print(e.reason)
nmTuitar = 0
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener) 

myStream.filter(follow=["49751816"])
