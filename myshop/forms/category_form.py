""" Libor Havránek App Copyright (C)  20.4 2023 """

from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired, ValidationError
from myshop.models.brand_model import Brand


class CategoryForm(FlaskForm):
    csrf_token = HiddenField()
    category_name = StringField('Značka:', validators=[DataRequired()])
    add_category_submit = SubmitField('Přidat kategorii')
    edit_category_submit = SubmitField('Upravit kategorii')

    def validate_category_name(self, brand_name):
        if len(brand_name.data.strip()) < 2:
            flash('Kategorie musí mít alespoň dva znaky.', 'error')
            raise ValidationError('Kategorie musí mít alespoň dva znaky.')

        brand = Brand.query.filter_by(brand_name=brand_name.data).first()
        if brand:
            flash('Tato kategorie je už zaregistrována v naší databázi.', 'error')
            raise ValidationError('Tato kategorie je už zaregistrována v naší databázi.')
