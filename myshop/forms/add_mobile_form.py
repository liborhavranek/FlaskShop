""" Libor Havránek App Copyright (C)  12.5 2023 """

from flask import flash
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, SubmitField, TextAreaField, SelectField, DecimalField, IntegerField, HiddenField, \
    FileField, MultipleFileField, FloatField, BooleanField
from wtforms.validators import InputRequired, Length, Optional, NumberRange, ValidationError

from myshop.models.brand_model import Brand
from myshop.models.category_model import Category
from myshop.models.product_model import Product


class MobileForm(FlaskForm):
    csrf_token = HiddenField()
    product_name = StringField('Název *:', validators=[InputRequired(), Length(max=80)])
    price = DecimalField('Cena *:', validators=[InputRequired(), NumberRange(min=0, max=999999.99)], default=0)
    discount = IntegerField('Sleva:', validators=[NumberRange(min=0, max=100)], default=0)
    stock = IntegerField('Počet kusů:', validators=[InputRequired(), NumberRange(min=0)], default=0)
    description = TextAreaField('Popis *:', validators=[InputRequired()], render_kw={'rows': 10})
    subheading = TextAreaField('Podnadpis *:', validators=[InputRequired()])
    display_size = DecimalField('Velikost displeje:', validators=[InputRequired(), NumberRange(min=0)])
    display_resolution = SelectField('Rozlišení displeje:', validators=[Optional()],
                                     choices=[('2160x1080', '2160 × 1080'), ('2280x1080', '2280 × 1080'),
                                              ('2300x1080', '2300 × 1080'), ('2310x1080', '2310 × 1080'),
                                              ('2340x1080', '2340 × 1080'), ('2388x1080', '2388 × 1080'),
                                              ('2400x1080', '2400 × 1080'), ('2436x1125', '2436 × 1125'),
                                              ('2460x1080', '2460 × 1080'), ('2520x1080', '2520 × 1080'),
                                              ('2532x1170', '2532 × 1170'), ('2636x1080', '2636 × 1080'),
                                              ('2688x1242', '2688 × 1242'), ('2778x1284', '2778 × 1284'),
                                              ('2408x1080', '2408 × 1080'), ('2640x1080', '2640 × 1080'),
                                              ('2800x1260', '2800 × 1260'), ('2848x1312', '2848 × 1312'),
                                              ('3040x1440', '3040 × 1440'), ('3120x1440', '3120 × 1440'),
                                              ('3200x1440', '3200 × 1440'), ('3216x1440', '3216 × 1440'),
                                              ('3840x1644', '3840 × 1644'), ('2176x1812', '2176 × 1812'),
                                              ('1280x600', '1280 × 600'), ('1334x750', '1334 × 750'),
                                              ('1480x720', '1480 × 720'), ('1520x720', '1520 × 720'),
                                              ('1560x720', '1560 × 720'), ('1600x720', '1600 × 720'),
                                              ('1650x720', '1650 × 720'), ('1792x828', '1792 × 828'),
                                              ('2142x876', '2142 × 876'), ('1080x540', '1080 × 540'),
                                              ('1200x540', '1200 × 540'), ('960x442', '960 × 442'),
                                              ('960x480', '960 × 480'), ('128x64', '128 × 64'),
                                              ('160x128', '160 × 128'), ('220x176', '220 × 176'),
                                              ('320x240', '320 × 240'), ('480x320', '480 × 320'), ])
    operating_system = SelectField('Operační systém:', choices=[('Android', 'Android'), ('iOS', 'iOS')], validators=[Optional()])
    operating_memory = IntegerField('Operační paměť:', validators=[InputRequired(), NumberRange(min=0)])
    memory = IntegerField('Velikost disku:', validators=[InputRequired(), NumberRange(min=0)])
    battery_capacity = IntegerField('Kapacita baterie:')
    memory_card_slot = BooleanField('Slot na paměťovou kartu:')
    face_id = BooleanField('Face ID:')
    touch_screen = BooleanField('Dotyková obrazovka:')
    front_camera = IntegerField('Přední kamera:')
    back_camera = IntegerField('Zadní kamera:')
    height = DecimalField('Výška:', validators=[InputRequired(), NumberRange(min=0, max=999999.99)], default=0)
    height_units = SelectField('Velikostní jednotka:', choices=[('cm', 'cm'), ('in', 'in'), ('mm', 'mm')], validators=[Optional()])
    width = DecimalField('Šířka:', validators=[InputRequired(), NumberRange(min=0, max=999999.99)], default=0)
    width_units = SelectField('Velikostní jednotka:', choices=[('cm', 'cm'), ('in', 'in'), ('mm', 'mm')], validators=[Optional()])
    depth = DecimalField('Hloubka:', validators=[InputRequired(), NumberRange(min=0, max=999999.99)], default=0)
    depth_units = SelectField('Velikostní jednotka:', choices=[('cm', 'cm'), ('in', 'in'), ('mm', 'mm')], validators=[Optional()])
    weight = DecimalField('Váha:', validators=[Optional(), NumberRange(min=0, max=999999.99)], default=0)
    weight_units = SelectField('Váhová jednotka:', choices=[('g', 'g'), ('kg', 'kg')], validators=[Optional()])
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
    convertible = BooleanField('Ohebný:')
    wifi = BooleanField('WiFi:')
    bluetooth = BooleanField('Bluetooth:')
    nfc = BooleanField('NFC:')
    processor = SelectField('Procesor:', choices=[
        ('Apple A14 Bionic', 'Apple A14 Bionic'),
        ('Qualcomm Snapdragon 888', 'Qualcomm Snapdragon 888'),
        ('Samsung Exynos 2100', 'Samsung Exynos 2100'),
        ('Apple A13 Bionic', 'Apple A13 Bionic'),
        ('Qualcomm Snapdragon 870', 'Qualcomm Snapdragon 870'),
        ('Qualcomm Snapdragon 865+', 'Qualcomm Snapdragon 865+'),
        ('Samsung Exynos 990', 'Samsung Exynos 990'),
        ('Qualcomm Snapdragon 855+', 'Qualcomm Snapdragon 855+'),
        ('Apple A12 Bionic', 'Apple A12 Bionic'),
        ('Qualcomm Snapdragon 845', 'Qualcomm Snapdragon 845'),
        ('Samsung Exynos 9820', 'Samsung Exynos 9820'),
        ('Huawei Kirin 990', 'Huawei Kirin 990'),
        ('Qualcomm Snapdragon 765G', 'Qualcomm Snapdragon 765G'),
        ('Samsung Exynos 980', 'Samsung Exynos 980'),
        ('Qualcomm Snapdragon 750G', 'Qualcomm Snapdragon 750G'),
        ('Qualcomm Snapdragon 730G', 'Qualcomm Snapdragon 730G'),
        ('Samsung Exynos 9611', 'Samsung Exynos 9611'),
        ('Qualcomm Snapdragon 710', 'Qualcomm Snapdragon 710'),
        ('Samsung Exynos 850', 'Samsung Exynos 850'),
        ('Qualcomm Snapdragon 662', 'Qualcomm Snapdragon 662'),
        ('Mediatek Helio G95', 'Mediatek Helio G95')
    ], validators=[Optional()])
    processor_cores = IntegerField('Počet jader:', validators=[InputRequired(), NumberRange(min=0)])
    esim = BooleanField('eSIM:')

    brand_id = SelectField('Značka:', coerce=int, choices=[], validators=[Optional()])
    category_id = SelectField('Kategorie:', coerce=int, choices=[], validators=[Optional()])

    product_image = FileField('Foto *:', validators=[InputRequired(), FileAllowed(['jpg', 'png', 'jpeg', 'webp'], 'Images only!')])
    additional_images = MultipleFileField('Další fotky:', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'webp'],
                                                                                    'Images only!')])

    add_product_submit = SubmitField('Přidat produkt')
    edit_product_submit = SubmitField('Upravit produkt')

    def __init__(self, *args, **kwargs):
        super(MobileForm, self).__init__(*args, **kwargs)
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
