
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
	token, token_secret = session['token']		
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback)
	auth.set_access_token(token,token_secret)
	user = tweepy.API(auth)
	singin = user.me()

	new_tweets = user.home_timeline(count=5)
	users = tweepy.Cursor(user.followers, screen_name=singin.name).items(5)
	return render_template('home.html',tweets=new_tweets,me=singin,users=users)


@app.route("/signup", methods=['GET','POST'])
def signup():
	if request.method == 'POST':
		message = " Account created !"
		fail = " Error in creating account please try again"
		email = request.form['email']
		password = request.form['confirmpassword']
		conn = mysql.connect
		cursor = conn.cursor()
		try:
			cursor.execute("Insert Into Users (email, password) VALUES ('" + email + "', '" + password + "')")
			conn.commit()
			return render_template('register.html',message=message,success=email)
		except Exception as e:
			print(e)
	return render_template('register.html',message=fail)

@app.route("/login", methods=['GET','POST'])
def login():
	if request.method =='POST':
		message = "Login failed invalid password !"
		yay = " successfully logged in ....... now what ?"
		email = str(request.form['email'])
		password = str(request.form['password'])
		conn = mysql.connect
		cursor = conn.cursor()
		cursor.execute("select password from Users where email ='"+email+"'")
		record = cursor.fetchall()
		if (len(record)==0):
			message = " No Account associated with that email"
			return render_template('register.html',message=message)
		for word in record:
			if password in word:
				return render_template('success.html',message=yay)
		return render_template('register.html',message=message)


	
@app.route("/analytics")
def analytics():
	return render_template('register.html')

@app.route("/tweet",methods=['GET','POST'])
def tweet():
	if request.method == 'POST':
		tweet = request.form['tweetbox']
		token, token_secret = session['token']		
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback)
		auth.set_access_token(token,token_secret)
		user = tweepy.API(auth)
		singin = user.me()
		user.update_status(tweet)
		singin = user.me()
		new_tweets = user.home_timeline(count=5)
		users = tweepy.Cursor(user.followers, screen_name=singin.name).items(10)
		return render_template('home.html',tweets=new_tweets,me=singin,users=users)


