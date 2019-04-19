from __future__ import absolute_import, print_function
import tweepy
import sys
import pandas
import json
import matplotlib

consumer_key="sd47vblI6MNSEXXOdQw26KUpn"
consumer_secret="z6IvOle6ImR3yGSJ5GLeudB0XMfjUOt3MFPPHtdVy5zw8QyjFV"
access_token="513405864-ocNwIksfXSgjImZHlM2HuinDGmYfpnpFJbNIIC1Z"
access_token_secret="UI9YBbbaExHZwPtKo96aGiUQzxX8QO2qv5Gvr8vKnGn4w"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)
tweettext=[]
OUTPUT_FILE = "tweetdata.txt"


class MyStreamListener(tweepy.StreamListener):
	def __init__(self):
		super().__init__()
		self.counter = 0
		self.limit = 20
		self.file = open(OUTPUT_FILE, "w")

	def on_status(self, status):
		tweet = status._json
		self.file.write( json.dumps(tweet) + '\n' )
		self.counter += 1
		if self.counter < self.limit:
			print("Number of tweets captured so far: {}".format(self.counter))
			return True
		else:
			self.file.close()
			myStream.disconnect()

	def on_error(self, status_code):
		if status_code == 420:
 		#returning False in on_data disconnects the stream
			return False

    


myStream = tweepy.Stream(auth, listener=MyStreamListener())

#LOCATIONS = [-64.0084,10.001,-59.1744,18.9787,
#			 -79.41,16.54,-75.26,19.01,
#			 -81.97,18.65,-79.12,20.32,
#			 -78.95,23.99,-76.95,25.24,
#			 -74.15,20.71,-70.54,22.49]    

#languages = ['en']
track = ['GameofThrons','jamie','Bran','Champions League']

new_tweets=myStream.filter(track=track)

tweets_data = []
with open(OUTPUT_FILE, "r") as tweets_file:
    # Read in tweets and store in list
    for line in tweets_file:
        tweet = json.loads(line)
        tweets_data.append(tweet)

df = pandas.DataFrame(tweets_data, columns=['created_at','lang', 'words', 'source'])
df.head()

df['created_at'] = pandas.to_datetime(df.created_at)
# Regular expression to get only what's between HTML tags: > <
df['source'] = df['source'].str.extract('>(.+?)<', expand=False).str.strip() 
df['words'] = df['source'].str.extract('>(.+?)<', expand=False).str.strip()
# Check DataFrame head again
df.head()

print(df.lang.value_counts())

print(df.source.value_counts())

print(df.words.value_counts())

lang_mask = (df.lang == 'en') | (df.lang == 'ca') | (df.lang == 'fr') | (df.lang == 'es')
source_mask = (df.source == 'Twitter for iPhone') | (df.source == 'Twitter for Android')\
    | (df.source == 'Twitter Web Client') | (df.source == 'Twitter for iPad') \
    | (df.source == 'Twitter Lite') | (df.source == 'Tweet Old Post')
track_mask =(df.words=='GameofThrones') | (df.words=='jamie') | (df.words=='Bran') | (df.words=='Champion League')

