from flask import render_template, redirect, url_for, request, flash
from flask.ext.login import login_required
from app import app, db, lm
from .models import User, Goals, NestConfig
import os

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		email = request.form['username']
		password = request.form['password']
		if valid_login(email, password):
			if check_user_in_db(email):
				return render_template('setup.html', email=email, password=password)
			else:
				return render_template('home.html')
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
		if user.email == email:
			return False
	return True

@app.route('/setup', methods=['GET', 'POST'])
def setup():
	habitatEmail = email
	nestPassword = password
	bankAccount = request.form['account']
	monthly = request.form['goal']
	limit = request.form['max']
	state = request.form['state']
	acSize = request.form['size']
	if acSize == 'empty':
		return render_template('setup.html', email=email, bankAccount=bankAccount, password=password)
	u = User(email=habitatEmail, bankAccount=bankAccount, fullName = fullName)
	#db.session.add(u)
	#db.session.commit()
	#g = Goals(monthly=monthly, maxlimit=limit, user_id=u)
	#db.session.add(p)
	#db.session.commit()
	return render_template('setup.html')

@app.route('/home')
def home():
	habitatEmail = email
	return render_template('home.html')

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))