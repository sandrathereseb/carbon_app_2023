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
  submit = SubmitField('Submit')  

class PlaneForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  submit = SubmitField('Submit')
  
class FerryForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  brought_on = SelectField('How are you riding the ferry', [InputRequired()],
    choices=[('On Foot', 'On Foot'), ('By Car', 'By Car')])
  submit = SubmitField('Submit')  

class MotorbikeForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  submit = SubmitField('Submit')

class BikeWalkForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  submit = SubmitField('Submit')  

class TramForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  submit = SubmitField('Submit')

class TrainForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  submit = SubmitField('Submit')  
