from flask import render_template, Blueprint, request, redirect, url_for, flash
from capp.models import Transport
from capp import db
from datetime import timedelta, datetime
from flask_login import login_required, current_user
from capp.carbon_app.forms import BusForm, CarForm, PlaneForm, FerryForm, MotorbikeForm, BikeWalkForm, TramForm, TrainForm

carbon_app=Blueprint('carbon_app',__name__)

efco2={
    'Bus':{'Diesel':0.09,'CNG':0.11,'No Fossil Fuel':0},
    'Car':{'Petrol':0.18,'Diesel':0.16,'No Fossil Fuel':0},
    'Plane':{'Under 800km':0.157,'Between 800km and 3700km':0.13,'Over 3700km':0.105},
    'Ferry':{'On Foot':0.0187, 'By Car':0.12952}, #check document if it's done. weird shit happened
    'Motorbike':{'Petrol':0.11},
    'Tram':{'Electric':0.0421},
    'Train':{'Electric':0.11}} # yeah check the doc for this as well looks SUPER scuffed
#Carbon app, main page
@carbon_app.route('/carbon_app')
@login_required
def carbon_app_home():
    return render_template('carbon_app/carbon_app.html', title='carbon_app')

#New entry bus
@carbon_app.route('/carbon_app/new_entry_bus', methods=['GET','POST'])
@login_required
def new_entry_bus():
    form = BusForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Bus'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type'] find out why this is commented out

        co2 = float(kms) * efco2[transport][fuel]
        co2 = float("{:.2f}".format(co2))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2,  author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_bus.html', title='new entry bus', form=form)

#New entry car
@carbon_app.route('/carbon_app/new_entry_car', methods=['GET','POST'])
@login_required
def new_entry_car():
    form = CarForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Car'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]

        co2 = float("{:.2f}".format(co2))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2,  author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_car.html', title='new entry car', form=form)    

#New entry plane
@carbon_app.route('/carbon_app/new_entry_plane', methods=['GET','POST'])
@login_required
def new_entry_plane():
    form = PlaneForm()
    if form.validate_on_submit(): #make if/else staatements here on the different lengths
        kms = form.kms.data
        if (float(kms)< 800.00):
            fuel ='Under 800km'
        
        elif (float(kms)> 3700.00):
            fuel ='Over 3700km'
        
        else:
            fuel ='Between 800km and 3700km'

        transport = 'Plane'

        co2 = float(kms) * efco2[transport][fuel]
        co2 = float("{:.2f}".format(co2))

        emissions = Transport(kms=kms, transport=transport, fuel='Aviation Kerosene', co2=co2,  author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_plane.html', title='new entry plane', form=form)  

#New entry ferry
@carbon_app.route('/carbon_app/new_entry_ferry', methods=['GET','POST'])
@login_required
def new_entry_ferry():
    form = FerryForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.brought_on.data
        transport = 'Ferry'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]

        co2 = float("{:.2f}".format(co2))
        transport = 'Ferry, '+ fuel
        emissions = Transport(kms=kms, transport=transport, fuel='Heavy Fuel Oil', co2=co2,  author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_ferry.html', title='new entry ferry', form=form)     

#New entry motorbike
@carbon_app.route('/carbon_app/new_entry_motorbike', methods=['GET','POST'])
@login_required
def new_entry_motorbike():
    form = MotorbikeForm()
    if form.validate_on_submit():
        kms = form.kms.data
        transport = 'Motorbike'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * 0.11

        co2 = float("{:.2f}".format(co2))

        emissions = Transport(kms=kms, transport=transport, fuel='Petrol', co2=co2,  author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_motorbike.html', title='new entry motorbike', form=form) 

#New entry Biking or Walking
@carbon_app.route('/carbon_app/new_entry_bikewalk', methods=['GET','POST'])
@login_required
def new_entry_BikeWalk():
    form = BikeWalkForm()
    if form.validate_on_submit():
        kms = form.kms.data
        transport = 'Biking / Walking'

        co2 = float(kms) * 0
        co2 = float("{:.2f}".format(co2))

        emissions = Transport(kms=kms, transport=transport, fuel='No Fossil Fuel', co2=co2,  author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_bikewalk.html', title='new entry Biking or Walking', form=form)

#New entry Tram
@carbon_app.route('/carbon_app/new_entry_tram', methods=['GET','POST'])
@login_required
def new_entry_tram():
    form = TramForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = 'Electric'
        transport = 'Tram'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]

        co2 = float("{:.2f}".format(co2))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2,  author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_tram.html', title='new entry tram', form=form)

#New entry Train
@carbon_app.route('/carbon_app/new_entry_train', methods=['GET','POST'])
@login_required
def new_entry_train():
    form = TrainForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = 'Electric'
        transport = 'Train'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]

        co2 = float("{:.2f}".format(co2))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2,  author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_train.html', title='new entry train', form=form)

#Your data
@carbon_app.route('/carbon_app/your_data')
@login_required
def your_data():
    #Table
    entries = Transport.query.filter_by(author=current_user). \
        filter(Transport.date> (datetime.now() - timedelta(days=5))).\
        order_by(Transport.date.desc()).order_by(Transport.transport.asc()).all()
    return render_template('carbon_app/your_data.html', title='your_data', entries=entries)

#Delete emission
@carbon_app.route('/carbon_app/delete-emission/<int:entry_id>')
def delete_emission(entry_id):
    entry = Transport.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for('carbon_app.your_data'))
    
