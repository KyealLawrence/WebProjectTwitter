
from flask import Flask, request, jsonify, render_template,url_for,session,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
import tweepy
import sys
from random import randint
import os
from authlib.flask.client import OAuth



app = Flask(__name__)
mysql = MySQL(app)

SECRET_KEY = 'Please work'
app.secret_key = SECRET_KEY

consumer_key="SZDw1y6xV30grFmnNQcm7Wp4Z"
consumer_secret="r3xR5eVKMySvbTAc3mExgaZZw9NwLmzSbyYksi3E8GnDxYug7H"
access_token="513405864-ceWliYQUYlGGcg1FduKRDpHslL83eRDuI1z69aVK"
access_token_secret="mZB3zIWNQBAbHWmgfwmzTy9nHWlMHh7U7QHZ18Q3z2k9g"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
my_info= api.me()


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

@app.route("/profile")
def getprofile():
	token, token_secret = session['token']
	
	sql_select_Query = "INSERT INTO 'sessioninfo'('token', 'token_secret') VALUES (%s,%s)",(token,token_secret)
	cursor = mysql.connection.cursor()
	cursor.execute(sql_select_Query)
	connection.commit()
	connection.close()
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback)
	auth.set_access_token(token,token_secret)
	user = tweepy.API(auth)
	singin = user.me()

	followers = str(singin.followers_count)
	following = str(singin.friends_count)
	tweets = str(singin.statuses_count)
	favtweets = str(singin.favourites_count)
	x = randint(1,50)
	friend = tweepy.Cursor(user.followers, screen_name=singin.name).items(x)
	for f in friend:
		friendurl=f.profile_image_url
		friendname=f.name
		friendat=f.screen_name
		friendtweet=f.status.text

	new_tweets = user.user_timeline(count=20)


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
	request_token = session['request_token']
	del session['request_token']
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback)
	auth.request_token = request_token
	verifier = request.args.get('oauth_verifier')
	auth.get_access_token(verifier)
	session['token'] = (auth.access_token, auth.access_token_secret)
	return redirect('/profile')
    


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



@app.route("/friends")
def getfriends():
	return render_template('friends.html')

@app.route("/timeline")
def timeline():
	new_tweets = api.home_timeline(count=5)
	users = tweepy.Cursor(api.followers, screen_name=my_info.name).items(10)

	return render_template('home.html',tweets=new_tweets,me=my_info,users=users)