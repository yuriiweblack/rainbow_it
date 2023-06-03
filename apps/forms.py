from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username or email address*', validators=[DataRequired()])
    password = PasswordField('Password*', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('LOG IN')

