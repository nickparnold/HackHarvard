from app import db

class User(db.Model):
	id = db.Column(db.String(24), primary_key=True)
	fullName = db.Column(db.String(50), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)

	def __repr__(self):
		return '<User %r>' % (self.fullName)
