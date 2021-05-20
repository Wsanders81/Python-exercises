from ast import Str
from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Email, Optional, URL

class AddCupcakeForm(FlaskForm):
    flavor = StringField('Flavor', validators=[InputRequired(message="Must enter a flavor")])
    size = StringField('Size', validators=[InputRequired(message="Must enter a size")])
    rating = FloatField('Rating', validators=[InputRequired(message="Must enter a rating")])
    image = StringField('Image URL', validators=[Optional(), URL()])