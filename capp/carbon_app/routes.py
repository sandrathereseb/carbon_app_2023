from flask import render_template, Blueprint, request, redirect, url_for, flash
from capp.models import Transport
from capp import db
from datetime import timedelta, datetime
from flask_login import login_required, current_user
from capp.carbon_app.forms import BusForm, CarForm, PlaneForm, FerryForm, MotorbikeForm, BikeWalkForm, TramForm, TrainForm
import json

carbon_app=Blueprint('carbon_app',__name__)


efco2={
    'Bus':{'Diesel':0.09,'CNG':0.11,'No Fossil Fuel':0},
    'Car':{'Petrol':0.18,'Diesel':0.16,'No Fossil Fuel':0},
    'Plane':{'Under 800km':0.157,'Between 800km and 3700km':0.13,'Over 3700km':0.105},
    'Ferry':{'On Foot':0.0187, 'By Car':0.12952}, 
    'Motorbike':{'Petrol':0.11},
    'Tram':{'Electric':0.0421},
    'Train':{'Electric':0.11}} 
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
    if form.validate_on_submit(): 
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
        co2 = float(kms) * efco2[transport][fuel]
        co2 = float("{:.2f}".format(co2))
        transport = 'Ferry'
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
        transport = 'BikingWalking'
        co2 = float(kms) * 0
        co2 = float("{:.2f}".format(co2))
        emissions = Transport(kms=kms, transport=transport, fuel='No Fossil Fuel', co2=co2,  author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_bikewalk.html',title='new entry Biking or Walking', form=form)

#New entry Tram
@carbon_app.route('/carbon_app/new_entry_tram', methods=['GET','POST'])
@login_required
def new_entry_tram():
    form = TramForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = 'Electric'
        transport = 'Tram'
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
    
        #Emissions by category
    emissions_by_transport = db.session.query(db.func.sum(Transport.co2), Transport.transport). \
        filter(Transport.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        group_by(Transport.transport).order_by(Transport.transport.asc()).all()
    emission_transport = [0, 0, 0, 0, 0, 0, 0, 0]
    first_tuple_elements = []
    second_tuple_elements = []
    for a_tuple in emissions_by_transport:
        first_tuple_elements.append(a_tuple[0])
        second_tuple_elements.append(a_tuple[1])

    if 'Bus' in second_tuple_elements:
        index_bus = second_tuple_elements.index('Bus')
        emission_transport[1]=first_tuple_elements[index_bus]
    else:
        emission_transport[1]

    if 'Car' in second_tuple_elements:
        index_car = second_tuple_elements.index('Car')
        emission_transport[2]=first_tuple_elements[index_car]
    else:
        emission_transport[2]

    if 'Ferry' in second_tuple_elements:
        index_ferry = second_tuple_elements.index('Ferry')
        emission_transport[3]=first_tuple_elements[index_ferry]
    else:
        emission_transport[3]

    if 'Motorbike' in second_tuple_elements:
        index_motorbike = second_tuple_elements.index('Motorbike')
        emission_transport[4]=first_tuple_elements[index_motorbike]
    else:
        emission_transport[4]

    if 'Plane' in second_tuple_elements:
        index_plane = second_tuple_elements.index('Plane')
        emission_transport[5]=first_tuple_elements[index_plane]
    else:
        emission_transport[5]

    if 'Tram' in second_tuple_elements:
        index_tram = second_tuple_elements.index('Tram')
        emission_transport[6]=first_tuple_elements[index_tram]
    else:
        emission_transport[6]

    if 'Train' in second_tuple_elements:
        index_train = second_tuple_elements.index('Train')
        emission_transport[7]=first_tuple_elements[index_train]
    else:
        emission_transport[7]


    #Kilometers by category
    kms_by_transport = db.session.query(db.func.sum(Transport.kms), Transport.transport). \
        filter(Transport.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        group_by(Transport.transport).order_by(Transport.transport.asc()).all()
    kms_transport = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    first_tuple_elements = []
    second_tuple_elements = []
    for a_tuple in kms_by_transport:
        first_tuple_elements.append(a_tuple[0])
        second_tuple_elements.append(a_tuple[1])

    if 'Bus' in second_tuple_elements:
        index_bus = second_tuple_elements.index('Bus')
        kms_transport[1]=first_tuple_elements[index_bus]
    else:
        kms_transport[1]

    if 'Car' in second_tuple_elements:
        index_car = second_tuple_elements.index('Car')
        kms_transport[2]=first_tuple_elements[index_car]
    else:
        kms_transport[2]

    if 'Ferry' in second_tuple_elements:
        index_ferry = second_tuple_elements.index('Ferry')
        kms_transport[3]=first_tuple_elements[index_ferry]
    else:
        kms_transport[3]

    if 'Motorbike' in second_tuple_elements:
        index_motorbike = second_tuple_elements.index('Motorbike')
        kms_transport[4]=first_tuple_elements[index_motorbike]
    else:
        kms_transport[4]

    if 'Plane' in second_tuple_elements:
        index_plane = second_tuple_elements.index('Plane')
        kms_transport[5]=first_tuple_elements[index_plane]
    else:
        kms_transport[5]

    if 'Tram' in second_tuple_elements:
        index_tram = second_tuple_elements.index('Tram')
        kms_transport[6]=first_tuple_elements[index_tram]
    else:
        kms_transport[6]

    if 'Train' in second_tuple_elements:
        index_train = second_tuple_elements.index('Train')
        kms_transport[7]=first_tuple_elements[index_train]
    else:
        kms_transport[7]

    if 'Biking&Walking' in second_tuple_elements:
        index_bikewalk = second_tuple_elements.index('Biking&Walking')
        kms_transport[8]=first_tuple_elements[index_bikewalk]
    else:
        kms_transport[8]

    #Emissions by date (individual)
    emissions_by_date = db.session.query(db.func.sum(Transport.co2), Transport.date). \
        filter(Transport.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        group_by(Transport.date).order_by(Transport.date.asc()).all()
    over_time_emissions = []
    dates_label = []
    for co2, date in emissions_by_date:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_emissions.append(co2)    

    #Kms by date (individual)
    kms_by_date = db.session.query(db.func.sum(Transport.kms), Transport.date). \
        filter(Transport.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        group_by(Transport.date).order_by(Transport.date.asc()).all()
    over_time_kms = []
    dates_label = []
    for co2, date in kms_by_date:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_kms.append(co2)      

    return render_template('carbon_app/your_data.html', title='your_data', entries=entries,
        emissions_by_transport_python_dic=emissions_by_transport,     
        emission_transport_python_list=emission_transport,             
        emissions_by_transport=json.dumps(emission_transport),
        kms_by_transport=json.dumps(kms_transport),
        over_time_emissions=json.dumps(over_time_emissions),
        over_time_kms=json.dumps(over_time_kms),
        dates_label=json.dumps(dates_label))

#Delete emission
@carbon_app.route('/carbon_app/delete-emission/<int:entry_id>')
def delete_emission(entry_id):
    entry = Transport.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for('carbon_app.your_data'))
    
