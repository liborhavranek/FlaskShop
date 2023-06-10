""" Libor Havránek App Copyright (C)  20.4 2023 """

from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired, ValidationError
from myshop.models.category_model import Category


class CategoryForm(FlaskForm):
    csrf_token = HiddenField()
    category_name = StringField("Kategorie:", validators=[DataRequired()])
    add_category_submit = SubmitField("Přidat kategorii")
    edit_category_submit = SubmitField("Upravit kategorii")

    def validate_category_name(self, category_name):
        if len(category_name.data.strip()) < 2:
            flash("Kategorie musí mít alespoň dva znaky.", "error")
            raise ValidationError("Kategorie musí mít alespoň dva znaky.")

        category = Category.query.filter_by(category_name=category_name.data).first()
        if category:
            flash("Tato kategorie je už zaregistrována v naší databázi.", "error")
            raise ValidationError(
                "Tato kategorie je už zaregistrována v naší databázi."
            )
