from myapp import myFLask
from flask import render_template, request, flash, redirect
from myapp.forms import TopCities
from myapp import db
from myapp.models import citydata

@myFlask.route("/", methods = ['GET' , 'POST'])
def hello():
	name = 'Bao Thien Vu'
	title = 'Top Cities'
	form =  TopCities()
	db.create_all()
	cities = citydata.query.all()
	
	if form.validate_on_submit():
		if db.session.query(citydata).filter_by(city_Rank = form.city_Rank.data).first():
			flash(f'{form.city_Name.data} was added')			
			name = request.form['city_Name']
			rank = len(citydata)
			city = citydata(name, rank)
			db.session.add(city)
			db.session.commit()
			return redirect('/')
		name = request.form['city_Name']
		rank = request.form['city_Rank']
		flash(f'{form.city_Name.data} was added')			
		city = citydata(name, rank)		
		db.session.add(city)
		db.session.commit()	
		
		return redirect('/')
	return render_template('home.html',name=name,title=title,form=form,cities=cities)

	