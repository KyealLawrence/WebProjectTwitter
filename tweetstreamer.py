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
tweettext=[]
class MyStreamListener(tweepy.StreamListener):
	def __init__(self):
		super().__init__()
		self.counter = 0
		self.limit = 10

	def on_status(self, status):
		tweettext.append(status.text)
		tweettext.append(status.user.location)
		self.counter += 1
		if self.counter < self.limit:
			print("Number of tweets captured so far: {}".format(self.counter))
			return True
		else:
			myStream.disconnect()

	def on_error(self, status_code):
		if status_code == 420:
 		#returning False in on_data disconnects the stream
			return False

    


myStream = tweepy.Stream(auth=api.auth, listener=MyStreamListener())

LOCATIONS = [-64.0084,10.001,-59.1744,18.9787,
			 -79.41,16.54,-75.26,19.01,
			 -81.97,18.65,-79.12,20.32,
			 -78.95,23.99,-76.95,25.24,
			 -74.15,20.71,-70.54,22.49]    

languages = ['en']
track = ['iphone']

myStream.filter(track=['python'])

def finder(word,array):
	count = 0
	for x in array:
		if word in x:
			count=count +1
	return count

numbers = []
searchedwords=[]

word = "iphone"
#total = finder(word,tweettext)




print(tweettext)

