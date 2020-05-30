import tweepy
import time

auth = tweepy.OAuthHandler("Nfk8RBzo9FffsIxZhw9myBgdR","dNVMj4XI0uiBMuvhbMCxaAZisELlHG7HntW3p36LPeH5XiAk88")

auth.set_access_token('1266653208862011392-k36RwrirSY4ePvau93Ru3BYZKSOaR1','phMcrFpLv3av7rZ4Cr21hBJMiMvtmx6wOoTrVjeNrcPL2')

api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

user = api.me()

search='devops'

number_of_tweets=100

for tweet in tweepy.Cursor(api.search,search).items(number_of_tweets):
    try:
        print("Tweeted")
        tweet.retweet()
        time.sleep(60)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break