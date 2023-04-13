""" Libor Havránek App Copyright (C)  13.4 2023 """

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired


class BrandForm(FlaskForm):
    csrf_token = HiddenField()
    brand_name = StringField('Značka:', validators=[DataRequired()])
    submit = SubmitField('Přidat značku')
