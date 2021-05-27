
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField, PasswordField
from wtforms.validators import InputRequired, Email, Optional, URL


class RegistrationForm(FlaskForm): 
    username = StringField("Username", validators=[InputRequired(message="Username required")])
    password = PasswordField("Password", validators = [InputRequired(message="Password required")])
    email = StringField("Email", validators=[InputRequired(message="Email address required"), Email(message="Please enter a valid email address")])
    first_name = StringField("First Name", validators=[InputRequired(message="First name required")])
    last_name = StringField("Last Name", validators=[InputRequired(message="Last name required")])

class LoginForm(FlaskForm): 
    username = StringField("Username", validators=[InputRequired(message="Username required")])
    password = PasswordField("Password", validators = [InputRequired(message="Password required")])
    
class FeedbackForm(FlaskForm): 
    #*** Max length of 30
    title = StringField('Title', validators=[InputRequired(message="Title required")])
    content = StringField('Content', validators=[InputRequired(message="Content required")])
    
