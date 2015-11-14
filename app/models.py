from app import db

class User(db.Model):
	id = db.Column(db.Integer, index=True, primary_key=True)
	email = db.Column(db.String(50),index=True, unique=True)
	bankAccount = db.Column(db.String(24), index=True)
	password = db.Column(db.String(50), index=True, unique=True)
	goals = db.relationship('Goals', backref='consumer', lazy='dynamic')
	nestConfig = db.relationship('NestConfig', backref='consumer', lazy='dynamic')

	def __init__(self, bankAccount, email, password, goals, nestConfig):
		self.bankAccount = bankAccount
		self.email = email
		self.password = password
		self.goals = goals
		self.nestConfig = nestConfig

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return unicode(self.id)

	def __repr__(self):
		return '<User %r>' % (self.fullName)

class Goals(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	monthly = db.Column(db.Numeric)
	maxlimit = db.Column(db.Numeric)
	state = db.Column(db.String(15))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Goals %r %r>' % (self.max), (self.monthly)

class NestConfig(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	hvac_state = db.Column(db.Boolean)
	temp = db.Column(db.Integer)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<NestConfig %r %r>' % (self.hvac_state), (self.temp)