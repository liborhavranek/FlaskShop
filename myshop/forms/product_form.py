""" Libor Havránek App Copyright (C)  20.4 2023 """

from flask import flash
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, SubmitField, TextAreaField, SelectField, DecimalField, IntegerField, HiddenField, \
    FileField, MultipleFileField
from wtforms.validators import InputRequired, Length, Optional, NumberRange, ValidationError

from myshop.models.brand_model import Brand
from myshop.models.category_model import Category
from myshop.models.product_model import Product


class ProductForm(FlaskForm):
    csrf_token = HiddenField()
    product_name = StringField('Název:', validators=[InputRequired(), Length(max=80)])
    price = DecimalField('Cena:', validators=[InputRequired(), NumberRange(min=0, max=999999.99)], default=0)
    discount = IntegerField('Sleva:', validators=[NumberRange(min=0, max=100)], default=0)
    stock = IntegerField('Počet kusů:', validators=[InputRequired(), NumberRange(min=0)], default=0)
    size = DecimalField('Velikost:', validators=[InputRequired(), NumberRange(min=0, max=999999.99)], default=0)
    size_units = SelectField('Velikostní jednotka:', choices=[('cm', 'cm'), ('in', 'in')], validators=[Optional()])
    weight = DecimalField('Váha:', validators=[Optional(), NumberRange(min=0, max=999999.99)], default=0)
    weight_units = SelectField('Váhová jednotka:', choices=[('g', 'g'), ('kg', 'kg')], validators=[Optional()])
    color = SelectField('Barva:', validators=[Optional()], choices=[('cerna', 'černá'), ('bila', 'bílá'),
                        ('seda', 'šedá'), ('hneda', 'hnědá'), ('tmava_hneda', 'tmavě hnědá'),
                        ('svetla_hneda', 'světle hnědá'), ('modra', 'modrá'), ('tmava_modra', 'tmavě modrá'),
                        ('svetla_modra', 'světle modrá'), ('zelena', 'zelená'), ('tmava_zelena', 'tmavě zelená'),
                        ('svetla_zelena', 'světle zelená'), ('zluta', 'žlutá'), ('oranzova', 'oranžová'),
                        ('cervena', 'červená'), ('ruzova', 'růžová'), ('fialova', 'fialová')])

    subheading = TextAreaField('Podnadpis:', validators=[InputRequired()])
    description = TextAreaField('Popis:', validators=[InputRequired()], render_kw={'rows': 10})
    brand_id = SelectField('Značka:', coerce=int, choices=[], validators=[Optional()])
    category_id = SelectField('Kategorie:', coerce=int, choices=[], validators=[Optional()])

    product_image = FileField('Hlavní obrázek:', validators=[InputRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    additional_images = MultipleFileField('Další obrázky:', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])

    add_product_submit = SubmitField('Přidat produkt')
    edit_product_submit = SubmitField('Upravit produkt')

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.brand_id.choices = [(brand.id, brand.brand_name) for brand in Brand.query.all()]
        self.category_id.choices = [(category.id, category.category_name) for category in Category.query.all()]

    def validate_product_name(self, product_name):
        if len(product_name.data.strip()) < 2:
            flash('Produkt musí mít alespoň dva znaky.', 'error')
            raise ValidationError('Produkt musí mít alespoň dva znaky.')

        product = Product.query.filter_by(product_name=product_name.data).first()
        if product:
            flash('Tento produkt je už zaregistrován v naší databázi.', 'error')
            raise ValidationError('Tento produkt je už zaregistrován v naší databázi.')

    def validate_subheading(self, subheading):
        if len(subheading.data.strip()) < 20:
            flash('Podnadpis musí mít alespoň dvacet znaků.', 'error')
            raise ValidationError('Podnadpis musí mít alespoň dvacet znaků.')

    def validate_description(self, subheading):
        if len(subheading.data.strip()) < 50:
            flash('Popis musí mít alespoň padesát znaků.', 'error')
            raise ValidationError('Popis musí mít alespoň padesát znaků.')

    def validate_price(self, price):
        if price.data == 0:
            flash('Cena produktu nemůže být nulová.', 'error')
            raise ValidationError('Cena produktu nemůže být nulová.', 'error')

