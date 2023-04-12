from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    csrf_token = HiddenField()
    email = StringField('Email:', validators=[DataRequired(), Email()])
    password = PasswordField('Heslo:', validators=[DataRequired()])
    submit = SubmitField('Přihlásit')
