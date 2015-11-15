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

				#conserverEnergy();
				bills = [0, 0, 0, 0, 0, 160.40, 195.23, 203.04, 161.86, 134.45, 0]
				days = [3, 7, 10, 12, 16, 21, 34, 38, 42, 47, 50, 54, 58, 57, 62]
				monthGraph = monthly.makeGraph(u.id, days, u.monthly, u.maxlimit)
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
		u = User(id='rashidajones@mailinator.com', bankAccount=bankAccount, password='ApplesOranges123!', monthly=monthly, maxlimit=limit, state=state, acUnit=acSize)
		db.session.add(u)
		db.session.commit()
		u = User.query.filter_by(id=email).first();
		bills = [0, 0, 0, 0, 0, 160.40, 195.23, 203.04, 161.86, 134.45, 0]
		days = [3, 7, 10, 12, 16, 21, 34, 38, 42, 47, 50, 54, 58, 57, 62]
		monthGraph = monthly.makeGraph(u.id, days, u.monthly, u.maxlimit)
		yearGraph = yearly.makeGraph(u.id, bills)
		#conserveEnergy(email);
		return render_template('home.html', monthly=u.monthly, maxlimit=u.maxlimit, monthGraph=monthGraph, yeartodate=yearGraph)
	else:
		return render_template('index.html')

@app.route('/home')
def home():
	u = User.query.filter_by(id=email).first();
	bills = [0, 0, 0, 0, 0, 160.40, 195.23, 203.04, 161.86, 134.45, 0]
	days = [3, 7, 10, 12, 16, 21, 34, 38, 42, 47, 50, 54, 58, 57, 62]
	monthGraph = monthly.makeGraph(u.id, days, u.monthly, u.maxlimit)
	yearGraph = yearly.makeGraph(u.id, bills)
	return render_template('home.html', monthly=u.monthly, maxlimit=u.maxlimit, monthGraph=monthGraph, yeartodate=yearGraph)

@app.route('/logout')
def logout():
	return redirect(url_for('index'))

@app.template_filter('money')
def money(s):
	return "%.2f" % s

def conserveEnergy(email):
	u = User.query.filter_by(id=email).first()
	statistics.energyStats(u.id, u.password, u.state, u.acUnit)
	u.timedeg = calibrate(u.id, u.password)
	return