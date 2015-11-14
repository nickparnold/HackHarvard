from flask import render_template
from app import app

@app.route('/')
@app.route('/login')
def login():
	return render_template('index.html')

@app.route('/setup')
def setup():
	return "setup page"

@app.route('/home')
def home():
	return "home automation page"