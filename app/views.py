from flask import render_template, redirect, url_for, request, flash
from flask.ext.login import login_required
from app import app, db, lm
from .models import User
import monthly
import yearly
import os

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		global email 
		email = request.form['username']
		global password 
		password = request.form['password']
		if valid_login(email, password):
			if check_user_in_db(email):
				return render_template('setup.html')
			else:
				global u
				u = User.query.filter_by(id=email).first();
				return render_template('home.html', monthly=u.monthly, maxlimit=u.maxlimit)
	else:
			error = 'Invalid email/password'
	return render_template('index.html',error=error)

def valid_login(username, password):
	value = os.system("nest.py --user %s --password %s curtemp" % (username, password))
	if value != 256:
		return True
	else:
		return False

def check_user_in_db(email):
	habitats = User.query.all()
	for user in habitats:
		if user.id == email:
			return False
	return True

@app.route('/setup', methods=['GET', 'POST'])
def setup():
	if request.method == 'POST':
		bankAccount = request.form['account']
		monthly = request.form['goal']
		limit = request.form['max']
		state = request.form['state']
		acSize = request.form['size']
		if acSize == 'empty':
			return render_template('setup.html', email=email, password=password)
		u = User(id=email, bankAccount=bankAccount, password=password, monthly=monthly, maxlimit=limit, state=state, acUnit=acSize)
		db.session.add(u)
		db.session.commit()
		return render_template('home.html', monthly=u.monthly, maxlimit=u.maxlimit)
	else:
		return render_template('index.html')

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.template_filter('money')
def money(s):
	return "%.2f" % s