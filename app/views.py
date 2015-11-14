from flask import render_template, redirect, url_for, request
from app import app, db, lm
from .models import User
import os

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if valid_login(request.form['username'], request.form['password']):
			return redirect(url_for('home'))
	else:
			error = 'Invalid email/password'
	return render_template('index.html',error=error)

def valid_login(username, password):
	value = os.system("nest.py --user %s --password %s curtemp" % (username, password))
	if value != 256:
		return True
	else:
		return False

@app.route('/setup')
def setup():
	return "setup page"

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))