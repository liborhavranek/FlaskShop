""" Libor Havránek App Copyright (C)  5.6. 2023 """


from flask import flash
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, SubmitField, TextAreaField, SelectField, DecimalField, IntegerField, HiddenField, \
    FileField, MultipleFileField, BooleanField
from wtforms.validators import InputRequired, Length, Optional, NumberRange, ValidationError

from myshop.models.brand_model import Brand
from myshop.models.category_model import Category
from myshop.models.product_model import Product


class ConsoleForm(FlaskForm):
    csrf_token = HiddenField()
    product_name = StringField('Název *:', validators=[InputRequired(), Length(max=80)])
    price = DecimalField('Cena *:', validators=[InputRequired(), NumberRange(min=0, max=999999.99)], default=0)
    discount = IntegerField('Sleva:', validators=[NumberRange(min=0, max=100)], default=0)
    stock = IntegerField('Počet kusů:', validators=[NumberRange(min=0)], default=0)
    description = TextAreaField('Popis *:', validators=[InputRequired()], render_kw={'rows': 10})
    subheading = TextAreaField('Podnadpis *:', validators=[InputRequired()])

    color = SelectField('Barva:', validators=[Optional()], choices=[('cerna', 'černá'), ('bila', 'bílá'),
                                                                    ('seda', 'šedá'), ('hneda', 'hnědá'),
                                                                    ('tmava_hneda', 'tmavě hnědá'),
                                                                    ('svetla_hneda', 'světle hnědá'),
                                                                    ('modra', 'modrá'), ('tmava_modra', 'tmavě modrá'),
                                                                    ('svetla_modra', 'světle modrá'),
                                                                    ('zelena', 'zelená'),
                                                                    ('tmava_zelena', 'tmavě zelená'),
                                                                    ('svetla_zelena', 'světle zelená'),
                                                                    ('zluta', 'žlutá'), ('oranzova', 'oranžová'),
                                                                    ('cervena', 'červená'), ('ruzova', 'růžová'),
                                                                    ('fialova', 'fialová')])

    ssd = BooleanField('SSD Disk:', default=False)
    hdd = BooleanField('HDD Disk:', default=False)

    ssd_capacity = IntegerField('Velikost disku SSD:', validators=[InputRequired(), NumberRange(min=0)], default=0)
    hdd_capacity = IntegerField('Velikost disku HDD:', validators=[InputRequired(), NumberRange(min=0)], default=0)

    dvd_drive = BooleanField('DVD Mechanika:')

    brand_id = SelectField('Značka:', coerce=int, choices=[], validators=[Optional()])
    category_id = SelectField('Kategorie:', coerce=int, choices=[], validators=[Optional()])

    product_image = FileField('Foto *:', validators=[InputRequired(), FileAllowed(['jpg', 'png', 'jpeg', 'webp'], 'Images only!')])
    additional_images = MultipleFileField('Další fotky:', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'webp'],
                                                                                    'Images only!')])

    add_product_submit = SubmitField('Přidat produkt')
    edit_product_submit = SubmitField('Upravit produkt')

    def __init__(self, *args, **kwargs):
        super(ConsoleForm, self).__init__(*args, **kwargs)
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
