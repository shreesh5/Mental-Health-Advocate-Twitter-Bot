from twython import Twython, TwythonAuthError, TwythonRateLimitError
from credentials import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

def init_api():
    api = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return api

def search(twitter, query):
    statement = twitter.seach(q=query, count=1)
    tweets = statement['statuses']

    for tweet in tweets:
        text = str(tweet['text'].encode("utf-8"))
        print(text)
        
        new_text = text.replace("committed suicide","passed away by suicide")
        print(new_text)

        handle = str(tweet['user']['screen_name'])
        sent = "@" + handle + " " + new_text
        print(sent)

        tweet(twitter, sent)

def tweet(twitter, sent):

    if len(sent) <= 140:
        print("tweetable")
        twitter.update_status(status=sent)
    else:
        print("Exceeded 140 characters")



if __name__ == "__main__":
    twitter = init_api()
    query = "committed suicide"
    search(twitter, query)