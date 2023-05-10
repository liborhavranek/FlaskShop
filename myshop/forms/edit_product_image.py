""" Libor Havránek App Copyright (C)  9.5 2023 """

from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import SubmitField, HiddenField, FileField, MultipleFileField
from wtforms.validators import InputRequired


class EditProductMainImageForm(FlaskForm):
    csrf_token = HiddenField()
    product_image = FileField('Hlavní foto:', validators=[InputRequired(),
                                                          FileAllowed(['jpg', 'png', 'jpeg', 'webp'], 'Images only!')])
    edit_product_main_image_submit = SubmitField('Upravit fotku')
