
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
import tweepy
import sys
import random
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
