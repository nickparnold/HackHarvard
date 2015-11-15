from flask import render_template, redirect, url_for, request, flash
from flask.ext.login import login_required
from app import app, db, lm
from .models import User
import monthly
import yearly
import statistics
import os

global email 
global u

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		email = request.form['username']
		global password 
		password = request.form['password']
		if valid_login(email, password):
			if check_user_in_db(email):
				return render_template('setup.html')
			else:
				u = User.query.filter_by(id=email).first();
				conserverEnergy();
				bills = [32.5, 37.6, 49.9, 53.0, 69.1, 75.4, 76.5, 76.6, 70.7, 60.6, 45.1, 29.3]
				monthGraph = monthly.makeGraph(u.id, bills, u.monthly, u.maxlimit)
				yearGraph = yearly.makeGraph(u.id, bills)
				return render_template('home.html', monthly=u.monthly, maxlimit=u.maxlimit, monthGraph=monthGraph, yeartodate = yearGraph)
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
		u = User.query.filter_by(id=email).first();
		bills = [32.5, 37.6, 49.9, 53.0, 69.1, 75.4, 76.5, 76.6, 70.7, 60.6, 45.1, 29.3]
		monthGraph = monthly.makeGraph(u.id, bills, u.monthly, u.maxlimit)
		yearGraph = yearly.makeGraph(u.id, bills)
		conserveEnergy();
		return render_template('home.html', monthly=u.monthly, maxlimit=u.maxlimit, monthGraph=monthGraph, yeartodate=yearGraph)
	else:
		return render_template('index.html')

@app.route('/home')
def home():
	u = User.query.filter_by(id=email).first();
	bills = [32.5, 37.6, 49.9, 53.0, 69.1, 75.4, 76.5, 76.6, 70.7, 60.6, 45.1, 29.3]
	monthGraph = monthly.makeGraph(u.id, bills, u.monthly, u.maxlimit)
	yearGraph = yearly.makeGraph(u.id, bills)
	return render_template('home.html', monthly=u.monthly, maxlimit=u.maxlimit, monthGraph=monthGraph, yeartodate=yearGraph)

@app.route('/logout')
def logout():
	return redirect(url_for('index'))

@app.template_filter('money')
def money(s):
	return "%.2f" % s

def conserveEnergy():
	u = User.query.filter_by(id=email).first()
	statistics.energyStats(u.id, u.password)
	u.timedeg = calibrate(u.id, u.password)
	return