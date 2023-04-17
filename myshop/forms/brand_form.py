""" Libor Havránek App Copyright (C)  13.4 2023 """

from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired, ValidationError
from myshop.models.brand_model import Brand


class BrandForm(FlaskForm):
    csrf_token = HiddenField()
    brand_name = StringField('Značka:', validators=[DataRequired()])
    submit = SubmitField('Přidat značku', render_kw={"value": "Upravit značku"})

    def validate_brand_name(self, brand_name):
        if len(brand_name.data.strip()) < 2:
            flash('Značka musí mít alespoň dva znaky.', 'error')
            raise ValidationError('Značka musí mít alespoň dva znaky.')

        brand = Brand.query.filter_by(brand_name=brand_name.data).first()
        if brand:
            flash('Tato značka je už zaregistrována v naší databázi.', 'error')
            raise ValidationError('Tato značka je už zaregistrována v naší databázi.')