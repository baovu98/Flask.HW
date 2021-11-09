from myapp import db

class citydata(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	city_Name = db.Column(db.String(128), unique = True, index = True)
	city_Rank = db.Column(db.Integer, unique = True)

		

	def __repr__(self):
                return f'{self.city_Name}'