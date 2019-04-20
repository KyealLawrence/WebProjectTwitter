
from flask import Flask, request, jsonify, render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
import tweepy
import sys
from random import randint
import os

app = Flask(__name__)
mysql = MySQL(app)

consumer_key="sd47vblI6MNSEXXOdQw26KUpn"
consumer_secret="z6IvOle6ImR3yGSJ5GLeudB0XMfjUOt3MFPPHtdVy5zw8QyjFV"
access_token="513405864-ocNwIksfXSgjImZHlM2HuinDGmYfpnpFJbNIIC1Z"
access_token_secret="UI9YBbbaExHZwPtKo96aGiUQzxX8QO2qv5Gvr8vKnGn4w"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
my_info = api.me()



app.config['MYSQL_HOST'] = 'remotemysql.com'
app.config['MYSQL_USER'] = '6iY42OOgiZ'
app.config['MYSQL_PASSWORD'] = '0saospJkqw'
app.config['MYSQL_DB'] = '6iY42OOgiZ'
app.config['TEMPLATES_AUTO_RELOAD'] = True




@app.route("/")
def hello():
	return render_template('index.html')

@app.route("/table",methods=['GET'])
def table():
	sql_select_Query = "select * from Users"
	cursor = mysql.connection.cursor()
	cursor.execute(sql_select_Query)
	records = cursor.fetchall()
	return render_template('table.html',user=records)

@app.route("/filteredtweets",methods=['GET'])
def getfilteredtweets():
	filtered = tweepy.Cursor(api.search,q="gameofthrones").items(10)
	return render_template('tweets.html',tweets=filtered)

@app.route("/profile")
def getprofile():
	
	followers = str(my_info.followers_count)
	following = str(my_info.friends_count)
	tweets = str(my_info.statuses_count)
	favtweets = str(my_info.favourites_count)
	x = randint(1,100)
	friend = tweepy.Cursor(api.followers, screen_name=my_info.name).items(x)
	for f in friend:
		friendurl=f.profile_image_url
		friendname=f.name
		friendat=f.screen_name
		friendtweet=f.status.text


	new_tweets = api.user_timeline(count=10)


	user = {
		'username':my_info.name,
		'at':my_info.screen_name,
		'bio':my_info.description,
		'followers':followers,
		'following':following,
		'tweets':tweets,
		'favtweets':favtweets,
		'website':my_info.url,
		'datecreated':my_info.created_at,
		'profilepic':my_info.profile_image_url,
		'friendurl':friendurl,
		'friendname':friendname,
		'friendat':friendat,
		'friendtweet':friendtweet,
		'hometweets':new_tweets,
		}	

	return render_template('profile.html', user=user)


@app.route("/friends")
def getfriends():
	return render_template('friends.html')