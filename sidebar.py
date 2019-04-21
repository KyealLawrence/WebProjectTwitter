import tweepy
import sys
import time

consumer_key="SZDw1y6xV30grFmnNQcm7Wp4Z"
consumer_secret="r3xR5eVKMySvbTAc3mExgaZZw9NwLmzSbyYksi3E8GnDxYug7H"
access_token="513405864-ceWliYQUYlGGcg1FduKRDpHslL83eRDuI1z69aVK"
access_token_secret="mZB3zIWNQBAbHWmgfwmzTy9nHWlMHh7U7QHZ18Q3z2k9g"

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
    print("User Follower count \t:" + str(my_info.followers_count))
    print("User Screen name \t:" + user.screen_name)
    print("User Follower count \t:" + str(user.followers_count))
    print ("Status \t: "+ user.description)
    print("\n")
  


users = tweepy.Cursor(api.followers, screen_name=my_info.name).items()

while True:
    try:
        user = next(users)
        get_user_informations(user)
        time.sleep(3)
        user = next(users)
    except StopIteration:
        break
    

