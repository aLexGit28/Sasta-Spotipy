# Inside app/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length 

class LoginForm(FlaskForm):
    # Username field: Text input, must be provided.
    username = StringField('Username', 
                           validators=[DataRequired(), Length(min=2, max=30)])
    
    # Password field: Password input (hides characters), must be provided.
    password = PasswordField('Password', 
                             validators=[DataRequired()])
    
    # Submit button
    submit = SubmitField('Login')