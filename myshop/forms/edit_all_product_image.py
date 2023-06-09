""" Libor Havránek App Copyright (C)  10.5 2023 """

from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import SubmitField, HiddenField, MultipleFileField


class AddProductAdditionalImagesForm(FlaskForm):
    csrf_token = HiddenField()
    additional_images = MultipleFileField(
        "Další fotky:",
        validators=[FileAllowed(["jpg", "png", "jpeg", "webp"], "Images only!")],
    )
    add_product_additional_image_submit = SubmitField("Přidat fotky")
