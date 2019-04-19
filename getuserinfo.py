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

#other_user = api.get_user("missmoxxley")
my_info = api.me()

#print(other_user)

def get_user_informations(user):
	followers = str(my_info.followers_count)

	print("User ID \t:" + str(user.id))
	print("User image profil \t:" + user.profile_image_url)
	print("User Name \t:" + user.name)
	print("User URL \t:",user.url)
	print("User profil text color \t:" + user.profile_text_color)
	print("User background image \t:" + user.profile_background_image_url)
	print("User Follower count \t:" + followers)
	print("User Following count \t:" + str(user.friends_count))	
	print("User Screen name \t:" + user.screen_name)
	print("User Verified \t:" + str(user.verified))
	print("User Favorite count \t:" + str(user.favourites_count))	
	print("User Status count \t:" + str(user.statuses_count))	
	print("User Description \t:", user.description)
	print("User Follower count \t:" + str(user.followers_count))
	print("User Created at \t:" + str(user.created_at))
	if hasattr(user, 'time_zone'):
		print("User Time zone \t:" + str(user.time_zone))
		print("User UTC Offset \t:" + str(user.utc_offset))

get_user_informations(my_info)

#statuscount =str(my_info.statuses_count)
#followers = str(my_info.followers_count)
#following = str(my_info.friends_count)
#print(my_info.profile_image_url)
#print(my_info.profile_banner_url)
#print(my_info.name)
#print(my_info.screen_name)
#print("Followers "+followers)
#print("Following: "+following)
#print("Number of tweets : "+statuscount)

