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
tweettext=[]
class MyStreamListener(tweepy.StreamListener):
	def __init__(self):
		super().__init__()
		self.counter = 0
		self.limit = 10

	def on_status(self, status):
		print(status.user.profile_image_url_https)
		print(status.user.name+"  @"+status.user.screen_name+" Tweeted from "+status.source)
		tweettext.append(status.text)
		print("Tweet "+status.text)
		print("testing stuff")
		print(status.user.location)
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

    


myStream = tweepy.Stream(auth, listener=MyStreamListener())

LOCATIONS = [-64.0084,10.001,-59.1744,18.9787,
			 -79.41,16.54,-75.26,19.01,
			 -81.97,18.65,-79.12,20.32,
			 -78.95,23.99,-76.95,25.24,
			 -74.15,20.71,-70.54,22.49]    

languages = ['en']
track = ['GameofThrons','jamie','Bran','Champions League']

new_tweets=myStream.filter(locations=LOCATIONS,languages=languages,track=track)

def finder(word,array):
	count = 0
	for x in array:
		if word in x:
			count=count +1
	return count

numbers = []
searchedwords=[]

for i in range(len(track)):
	numbers.append(finder(track[i],tweettext))
	searchedwords.append(track[i])


print (numbers)
print(searchedwords)
