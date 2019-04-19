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

filtered = tweepy.Cursor(api.search,q="gameofthrones").items(10)


for tweets in filtered:
        print(tweets.user.profile_image_url_https)
        print(tweets.user.name+"  @"+tweets.user.screen_name+" Tweeted from "+tweets.source)
        print("Tweet "+tweets.text)
        print("testing stuff")
		
		# Have to get country info and quoted or retweet info
		#print(tweets.country)
		#print(tweets.place.country_code)
		#add more parameters to save stuff