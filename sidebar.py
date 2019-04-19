import tweepy
import sys
import time

consumer_key="sd47vblI6MNSEXXOdQw26KUpn"
consumer_secret="z6IvOle6ImR3yGSJ5GLeudB0XMfjUOt3MFPPHtdVy5zw8QyjFV"
access_token="513405864-ocNwIksfXSgjImZHlM2HuinDGmYfpnpFJbNIIC1Z"
access_token_secret="UI9YBbbaExHZwPtKo96aGiUQzxX8QO2qv5Gvr8vKnGn4w"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

my_info = api.get_user("KyealLawrence")

api = tweepy.API(auth,wait_on_rate_limit=True)

def get_user_informations(user):
    followers = str(my_info.followers_count)
    print("User ID \t:" + str(user.id))
    print("User image profil \t:" + user.profile_image_url)
    print("User Name \t:" + user.name)
    print("User Follower count \t:" + followers)
    print("User Screen name \t:" + user.screen_name)
    print("User Follower count \t:" + str(user.followers_count))
    print ("Status \t: "+ user.status.text)
    print("\n")
  


users = tweepy.Cursor(api.followers, screen_name="KyealLawrence").items()

while True:
    try:
        user = next(users)
        get_user_informations(user)
        time.sleep(3)
        user = next(users)
    except StopIteration:
        break
    

