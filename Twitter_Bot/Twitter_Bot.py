import tweepy
import time

auth = tweepy.OAuthHandler("Nfk8RBzo9FffsIxZhw9myBgdR", "dNVMj4XI0uiBMuvhbMCxaAZisELlHG7HntW3p36LPeH5XiAk88")

auth.set_access_token('1266653208862011392-TvTfrMVEZzJ7WfqgiFe5xGZt00zDIR','M0jodUsTlCB4z2vk4mNQ1eABZKmqaybJ6U3k84awMSxhS')

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
