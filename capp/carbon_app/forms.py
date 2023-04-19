from flask_wtf import FlaskForm
from wtforms import  SubmitField,  SelectField,  FloatField
from wtforms.validators import InputRequired

class BusForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Diesel', 'Diesel'), ('CNG', 'CNG'), ('No Fossil Fuel', 'No Fossil Fuel')])
  submit = SubmitField('Submit')

class CarForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('No Fossil Fuel', 'No Fossil Fuel')])
  passG = FloatField('Number of passengers', [InputRequired()]) #see if this works, this is the amount of passengers from the formula
  submit = SubmitField('Submit')  

class PlaneForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  type_of_trip = SelectField('How long was your trip', [InputRequired()], 
    choices=[('Under 800km', 'Under 800km'),('Between 800km and 3700km','Between 800km and 3700km'),('Over 3700km','Over 3700km')])
  submit = SubmitField('Submit')
  
class FerryForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  brought_on = SelectField('How are you riding the ferry', [InputRequired()],
    choices=[('On Foot', 'On Foot'), ('By Car', 'By Car')])
  submit = SubmitField('Submit')  

class MotorcycleForm(FlaskForm): #not yet done, see document
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Petrol', 'Petrol'), ('No Fossil Fuel', 'No Fossil Fuel')])
  submit = SubmitField('Submit')

class BikeWalkForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('No Fossil Fuel', 'No Fossil Fuel')])
  submit = SubmitField('Submit')  

class TramForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Electric', 'Electric')])
  submit = SubmitField('Submit')

class TrainForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Electric', 'Electric')])
  submit = SubmitField('Submit')  
