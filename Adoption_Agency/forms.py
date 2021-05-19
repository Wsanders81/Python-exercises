from flask_wtf import FlaskForm
# from sqlalchemy import Integer
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Email, Optional, ValidationError, URL, NumberRange

def validate_species(form, field): 
    species = ["cat", "dog", "porcupine"]
    if (field.data) not in species: 
        raise ValidationError("Species must be Cat, Dog, or Porcupine.")

class AddPet(FlaskForm): 
    name = StringField('Pet Name', validators=[InputRequired(message="Pet name cannot be blank")])
    species = SelectField('Species', choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')], 
                          validators=[InputRequired(), validate_species])
    photo_url = StringField("URL Photo of Pet", validators=[Optional(), URL()])
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=0, max=30, message="Please enter an age between 0 and 30")])
    notes = StringField('Notes', validators=[Optional()])
    available = BooleanField('Available')


    # , validators=[InputRequired(message="Pet must be available for adoption=")]