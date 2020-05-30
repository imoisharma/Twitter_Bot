# Incedge Bot

Incedge Bot is a Twitter Bot which will retweet DevOps, Machine Learning tweets, and like them in every 5 minutes. And, depolyment of this package is on <a href="https://www.heroku.com">Heroku: Cloud Application Platform</a>

## Twitter Bot Link

To see the demo go to the https://www.twitter.com/incedge_io

To run the same commands install the package below

```bash
pip install tweepy
```

## Usage

```python
import tweepy
import time

auth = tweepy.OAuthHandler("Key","Secret_Key")
auth.set_access_token("Key","Secret_Key")

api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

user = api.me()

search=['devops','ML']

number_of_tweets=1000

# Testing condition
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
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
