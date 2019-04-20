from __future__ import absolute_import, print_function
import tweepy
import sys


consumer_key="sd47vblI6MNSEXXOdQw26KUpn"
consumer_secret="z6IvOle6ImR3yGSJ5GLeudB0XMfjUOt3MFPPHtdVy5zw8QyjFV"
access_token="513405864-ocNwIksfXSgjImZHlM2HuinDGmYfpnpFJbNIIC1Z"
access_token_secret="UI9YBbbaExHZwPtKo96aGiUQzxX8QO2qv5Gvr8vKnGn4w"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)

new_tweets = api.user_timeline(count=10)

def get_tweets(tweets):
	for tweet in tweets:
		print(" Tweeter profile ult :"+tweet.user.profile_image_url_https)
		print(tweet.user.name+"  @"+tweet.user.screen_name+" Tweeted from "+tweet.source)
		print("Tweet Message : " + tweet.text)
		print("Tweet Favorited count \t:" + str(tweet.favorite_count))	
		print(tweet.user.location)
		# Display sender and mentions user
		if hasattr(tweet, 'retweeted_status'):
			print("Tweet send by : " + tweet.retweeted_status.user.screen_name)
			id_of_tweet=tweet.retweeted_status.id_str
			tweet = api.get_status(id=id_of_tweet)
			print("Original tweet : "+tweet.text)
		

get_tweets(new_tweets)
