from app import db

class User(db.Model):
	id = db.Column(db.String(24), primary_key=True)
	fullName = db.Column(db.String(50), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	goals = db.relationship('Goals', backref='consumer', lazy='dynamic')
	nestConfig = db.relationship('NestConfig', backref='consumer', lazy='dynamic')

	def __repr__(self):
		return '<User %r>' % (self.fullName)

class Goals(db.Model):
	goal_id = db.Column(db.Integer, primary_key=True)
	monthly = db.Column(db.Numeric)
	max = db.Column(db.Numeric)
	user_id = db.Column(db.String(24), db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Goals %r %r>' % (self.max), (self.monthly)

class NestConfig(db.Model):
	config_id = db.Column(db.Integer, primary_key=True)
	hvac_state = db.Column(db.Boolean)
	temp = db.Column(db.Integer)

	def __repr__(self):
		return '<NestConfig %r %r>' % (self.hvac_state), (self.temp)