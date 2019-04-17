
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL

import random
import os

app = Flask(__name__)
mysql = MySQL(app)


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