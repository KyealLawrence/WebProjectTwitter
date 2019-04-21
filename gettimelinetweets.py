from __future__ import absolute_import, print_function
import tweepy
import sys


consumer_key="SZDw1y6xV30grFmnNQcm7Wp4Z"
consumer_secret="r3xR5eVKMySvbTAc3mExgaZZw9NwLmzSbyYksi3E8GnDxYug7H"
access_token="513405864-ceWliYQUYlGGcg1FduKRDpHslL83eRDuI1z69aVK"
access_token_secret="mZB3zIWNQBAbHWmgfwmzTy9nHWlMHh7U7QHZ18Q3z2k9g"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)

new_tweets = api.home_timeline(count=10)

def get_tweets(tweets):
	for tweet in tweets:
		print(" Tweeter profile ult :"+tweet.user.profile_image_url_https)
		print(tweet.user.name+"  @"+tweet.user.screen_name+" Tweeted from "+tweet.source)
		print("Tweet Message : " + tweet.text)
		print("Tweet Favorited count \t:" + str(tweet.favorite_count))	
		print(tweet.user.location)
		print(tweet.created_at)
		# Display sender and mentions user
		if hasattr(tweet, 'retweeted_status'):
			print("Tweet send by : " + tweet.retweeted_status.user.screen_name)
			id_of_tweet=tweet.retweeted_status.id_str
			tweet = api.get_status(id=id_of_tweet)
			print("Original tweet : "+tweet.text)
		

get_tweets(new_tweets)
