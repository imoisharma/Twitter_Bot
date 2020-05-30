import tweepy
import time

auth = tweepy.OAuthHandler("Key", "Secret_Key")

auth.set_access_token('Key','Secret_Key')

api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

user = api.me()

search=['devops','ML']

number_of_tweets=1000

for tweet in tweepy.Cursor(api.search,search).items(number_of_tweets):
    try:
        print("Tweeted")
        tweet.retweet()
        tweet.favorite()
        time.sleep(60*5)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
