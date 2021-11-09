from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class TopCities(FlaskForm):
	city_Name = StringField('City Name',validators=[DataRequired()])
	city_Rank = IntegerField('City rank',validators=[DataRequired()])
	is_visited = BooleanField('Visited')
	submit = SubmitField('Submit')