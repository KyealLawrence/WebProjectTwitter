
from flask import Flask, request, jsonify, render_template,url_for,session,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
import tweepy
import sys
from random import randint
import os
from authlib.flask.client import OAuth
SECRET_KEY = 'development key'


app = Flask(__name__)
mysql = MySQL(app)
app.secret_key = SECRET_KEY
consumer_key="sd47vblI6MNSEXXOdQw26KUpn"
consumer_secret="z6IvOle6ImR3yGSJ5GLeudB0XMfjUOt3MFPPHtdVy5zw8QyjFV"
access_token="513405864-ocNwIksfXSgjImZHlM2HuinDGmYfpnpFJbNIIC1Z"
access_token_secret="UI9YBbbaExHZwPtKo96aGiUQzxX8QO2qv5Gvr8vKnGn4w"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)



app.config['MYSQL_HOST'] = 'remotemysql.com'
app.config['MYSQL_USER'] = '6iY42OOgiZ'
app.config['MYSQL_PASSWORD'] = '0saospJkqw'
app.config['MYSQL_DB'] = '6iY42OOgiZ'
app.config['TEMPLATES_AUTO_RELOAD'] = True




callback = 'https://floating-cliffs-24637.herokuapp.com/callback'

@app.route('/auth')
def auth():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback)
    url = auth.get_authorization_url()
    session['request_token'] = auth.request_token
    return redirect(url)

@app.route("/profile2")
def getprofile2():
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback)
	auth.set_access_token(token, token_secret)
	user = tweepy.API(auth)
	singin = user.me()
	
	followers = str(singin.followers_count)
	following = str(singin.friends_count)
	tweets = str(singin.statuses_count)
	favtweets = str(singin.favourites_count)
	x = randint(1,50)
	friend = tweepy.Cursor(api.followers, screen_name=singin.name).items(x)
	for f in friend:
		friendurl=f.profile_image_url
		friendname=f.name
		friendat=f.screen_name
		friendtweet=f.status.text


	new_tweets = api.user_timeline(count=20)


	user = {
		'username':singin.name,
		'at':singin.screen_name,
		'bio':singin.description,
		'followers':followers,
		'following':following,
		'tweets':tweets,
		'favtweets':favtweets,
		'website':singin.url,
		'datecreated':singin.created_at,
		'profilepic':singin.profile_image_url,
		'friendurl':friendurl,
		'friendname':friendname,
		'friendat':friendat,
		'friendtweet':friendtweet,
		'hometweets':new_tweets,
		}	

	return render_template('profile.html', user=user)

@app.route('/callback')
def twitter_callback():
	api = tweepy.API(auth)
	my_info = api.me()
    request_token = session['request_token']
    del session['request_token']
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback)
    auth.request_token = request_token
    verifier = request.args.get('oauth_verifier')
    auth.get_access_token(verifier)
    session['token'] = (auth.access_token, auth.access_token_secret)
    return redirect('/profile2')


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
	api = tweepy.API(auth)
	my_info = api.me()
	filtered = tweepy.Cursor(api.search,q="gameofthrones").items(10)
	return render_template('tweets.html',tweets=filtered)

@app.route("/profile")
def getprofile():
	api = tweepy.API(auth)
	my_info = api.me()
	followers = str(my_info.followers_count)
	following = str(my_info.friends_count)
	tweets = str(my_info.statuses_count)
	favtweets = str(my_info.favourites_count)
	x = randint(1,50)
	friend = tweepy.Cursor(api.followers, screen_name=my_info.name).items(x)
	for f in friend:
		friendurl=f.profile_image_url
		friendname=f.name
		friendat=f.screen_name
		friendtweet=f.status.text


	new_tweets = api.user_timeline(count=20)


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

@app.route("/test")
def signin():
	return render_template('singin.html')