from app import db

class User(db.Model):
	id = db.Column(db.String(50), index=True, unique=True, primary_key=True)
	bankAccount = db.Column(db.String(24), index=True)
	password = db.Column(db.String(50), index=True, unique=True)
	monthly = db.Column(db.Float, index=True)
	maxlimit = db.Column(db.Float, index=True)
	state = db.Column(db.String(15), index=True)
	acUnit = db.Column(db.String(10), index=True)
	dailyestimation = db.Column(db.Float, index=True)

	def __init__(self, id, bankAccount, password, monthly, maxlimit, state, acUnit):
		self.id = id
		self.bankAccount = bankAccount
		self.password = password
		self.monthly = monthly
		self.maxlimit = maxlimit
		self.state = state
		self.acUnit = acUnit

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return unicode(self.id)

	def __repr__(self):
		return '<User %r>' % (self.bankAccount)