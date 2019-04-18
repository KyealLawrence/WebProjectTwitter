from __future__ import absolute_import, print_function
import tweepy
import sys


consumer_key="sd47vblI6MNSEXXOdQw26KUpn"
consumer_secret="z6IvOle6ImR3yGSJ5GLeudB0XMfjUOt3MFPPHtdVy5zw8QyjFV"
access_token="513405864-ocNwIksfXSgjImZHlM2HuinDGmYfpnpFJbNIIC1Z"
access_token_secret="UI9YBbbaExHZwPtKo96aGiUQzxX8QO2qv5Gvr8vKnGn4w"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def get_all_tweets(screen_name):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)	
    alltweets = []	
    new_tweets = api.user_timeline(screen_name = screen_name,count=20)
    alltweets.extend(new_tweets)	
    oldest = alltweets[-1].id - 1
    while len(new_tweets) > 0:
        print ("getting tweets before %s" % (oldest))
        new_tweets = api.user_timeline(screen_name = screen_name,max_id=40)
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1
        print ("...%s tweets downloaded so far" % (len(alltweets)))
    for tweet in alltweets:
        print(tweet.user.name+": Tweet :"+tweet.text)



get_all_tweets("missmoxxley")
