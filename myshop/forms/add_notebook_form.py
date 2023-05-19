""" Libor Havránek App Copyright (C)  16.5 2023 """

from flask import flash
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from myshop.models.brand_model import Brand
from myshop.models.product_model import Product
from myshop.models.category_model import Category
from wtforms.validators import InputRequired, Length, Optional, NumberRange, ValidationError
from wtforms import StringField, SubmitField, TextAreaField, SelectField, DecimalField, IntegerField, HiddenField, \
    FileField, MultipleFileField, BooleanField


class NotebookForm(FlaskForm):
    csrf_token = HiddenField()
    product_name = StringField('Název *:', validators=[InputRequired(), Length(max=80)])
    price = DecimalField('Cena *:', validators=[InputRequired(), NumberRange(min=0, max=999999.99)], default=0)
    discount = IntegerField('Sleva:', validators=[NumberRange(min=0, max=100)], default=0)
    stock = IntegerField('Počet kusů:', validators=[NumberRange(min=0)], default=0)
    description = TextAreaField('Popis *:', validators=[InputRequired()], render_kw={'rows': 10})
    subheading = TextAreaField('Podnadpis *:', validators=[InputRequired()])

    display_size = DecimalField('Velikost displeje *:', validators=[InputRequired(), NumberRange(min=0)], default=0)
    display_resolution = SelectField('Rozlišení displeje *:', validators=[Optional()],
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
                                              ('1650x720', '720'), ('1792x828', '1792 × 828'),
                                              ('2142x876', '2142 × 876'), ('1080x540', '1080 × 540'),
                                              ('1200x540', '1200 × 540'), ('960x442', '960 × 442'),
                                              ('960x480', '960 × 480'), ('128x64', '128 × 64'),
                                              ('160x128', '160 × 128'), ('220x176', '220 × 176'),
                                              ('320x240', '320 × 240'), ('480x320', '480 × 320'), ])

    display_frequency = IntegerField('Frekvence obnovování:', validators=[NumberRange(min=0)], default=0)
    display_nits = IntegerField('Jas displeje:', validators=[NumberRange(min=0)], default=0)
    display_type = SelectField('Typ displeje:', choices=[
                                                        ('IPS', 'IPS'),
                                                        ('TFT', 'TFT'),
                                                        ('OLED', 'OLED'),
                                                        ('AMOLED', 'AMOLED'),
                                                        ('Super AMOLED', 'Super AMOLED'),
                                                        ('Retina', 'Retina'),
                                                        ('LCD', 'LCD'),
                                                        ('LED', 'LED'),
                                                        ('P-OLED', 'P-OLED'),
                                                        ('LTPS', 'LTPS'),
                                                        ('AMOLED Plus', 'AMOLED Plus'),
                                                        ('Dynamic AMOLED', 'Dynamic AMOLED'),
                                                        ('Fluid AMOLED', 'Fluid AMOLED'),
                                                        ('Mini-LED', 'Mini-LED'),
                                                        ('MicroLED', 'MicroLED'),
                                                    ], validators=[Optional()])

    processor = SelectField('Procesor:', choices=[
        ('Intel Core i3', 'Intel Core i3'),
        ('Intel Core i5', 'Intel Core i5'),
        ('Intel Core i7', 'Intel Core i7'),
        ('Intel Core i9', 'Intel Core i9'),
        ('AMD Ryzen 3', 'AMD Ryzen 3'),
        ('AMD Ryzen 5', 'AMD Ryzen 5'),
        ('AMD Ryzen 7', 'AMD Ryzen 7'),
        ('AMD Ryzen 9', 'AMD Ryzen 9'),
    ], validators=[Optional()])
    processor_cores = IntegerField('Počet jader:', validators=[NumberRange(min=0)], default=0)

    operating_memory = IntegerField('Operační paměť *:', validators=[InputRequired(), NumberRange(min=0)], default=0)

    graphics_card = SelectField('Grafická karta:', validators=[Optional()], choices=[
        ('NVIDIA GeForce GTX 1660 Ti', 'NVIDIA GeForce GTX 1660 Ti'),
        ('NVIDIA GeForce RTX 2060', 'NVIDIA GeForce RTX 2060'),
        ('NVIDIA GeForce RTX 3060', 'NVIDIA GeForce RTX 3060'),
        ('NVIDIA GeForce RTX 3070', 'NVIDIA GeForce RTX 3070'),
        ('NVIDIA GeForce RTX 3080', 'NVIDIA GeForce RTX 3080'),
        ('AMD Radeon RX 580', 'AMD Radeon RX 580'),
        ('AMD Radeon RX 6700 XT', 'AMD Radeon RX 6700 XT'),
        ('AMD Radeon RX 6800', 'AMD Radeon RX 6800'),
        ('AMD Radeon RX 6900 XT', 'AMD Radeon RX 6900 XT'),
        ('NVIDIA Quadro RTX 4000', 'NVIDIA Quadro RTX 4000'),
        ('NVIDIA Quadro RTX 5000', 'NVIDIA Quadro RTX 5000'),
        ('AMD Radeon Pro 5500M', 'AMD Radeon Pro 5500M'),
        ('AMD Radeon Pro 5600M', 'AMD Radeon Pro 5600M'),
        ('Intel UHD Graphics 630', 'Intel UHD Graphics 630'),
        ('AMD Radeon RX Vega 11', 'AMD Radeon RX Vega 11'),
        ('NVIDIA GeForce MX350', 'NVIDIA GeForce MX350'),
        ('NVIDIA GeForce MX450', 'NVIDIA GeForce MX450'),
        ('Intel Iris Xe Graphics G7', 'Intel Iris Xe Graphics G7'),
        ('AMD Radeon R7', 'AMD Radeon R7'),
        ('AMD Radeon R9', 'AMD Radeon R9'),
        ('NVIDIA GeForce GT 1030', 'NVIDIA GeForce GT 1030'),
        ('NVIDIA GeForce GT 710', 'NVIDIA GeForce GT 710'),
        ('Intel HD Graphics 620', 'Intel HD Graphics 620'),
        ('Intel HD Graphics 630', 'Intel HD Graphics 630'),
        ('AMD Radeon RX 5500M', 'AMD Radeon RX 5500M'),
        ('AMD Radeon RX 5600M', 'AMD Radeon RX 5600M'),
        ('NVIDIA GeForce GTX 1650 Ti', 'NVIDIA GeForce GTX 1650 Ti'),
        ('NVIDIA GeForce GTX 1660 Super', 'NVIDIA GeForce GTX 1660 Super'),
        ('NVIDIA GeForce RTX 3090', 'NVIDIA GeForce RTX 3090'),
        ('NVIDIA GeForce RTX 3080 Ti', 'NVIDIA GeForce RTX 3080 Ti'),
        ('AMD Radeon RX 570', 'AMD Radeon RX 570'),
        ('AMD Radeon RX 6700', 'AMD Radeon RX 6700'),
        ('AMD Radeon RX 6800 XT', 'AMD Radeon RX 6800 XT'),
        ('AMD Radeon RX 6800M', 'AMD Radeon RX 6800M'),
        ('NVIDIA Quadro RTX 3000', 'NVIDIA Quadro RTX 3000'),
        ('NVIDIA Quadro RTX 6000', 'NVIDIA Quadro RTX 6000'),
        ('AMD Radeon Pro 5300M', 'AMD Radeon Pro 5300M'),
        ('AMD Radeon Pro 5600M', 'AMD Radeon Pro 5600M'),
        ('Intel Iris Xe Graphics G7', 'Intel Iris Xe Graphics G7'),
        ('AMD Radeon R7', 'AMD Radeon R7'),
        ('AMD Radeon R9', 'AMD Radeon R9'),
        ('NVIDIA GeForce GT 1030', 'NVIDIA GeForce GT 1030'),
        ('NVIDIA GeForce GT 710', 'NVIDIA GeForce GT 710'),
        ('Intel HD Graphics 620', 'Intel HD Graphics 620'),
        ('Intel HD Graphics 630', 'Intel HD Graphics 630'),
        ('AMD Radeon RX 5500M', 'AMD Radeon RX 5500M'),
        ('AMD Radeon RX 5600M', 'AMD Radeon RX 5600M'),
        ('NVIDIA GeForce GTX 1650 Ti', 'NVIDIA GeForce GTX 1650 Ti'),
        ('NVIDIA GeForce GTX 1660 Super', 'NVIDIA GeForce GTX 1660 Super'),
        ('NVIDIA GeForce RTX 3090', 'NVIDIA GeForce RTX 3090'),
        ('NVIDIA GeForce RTX 3080 Ti', 'NVIDIA GeForce RTX 3080 Ti'),
        ('AMD Radeon RX 570', 'AMD Radeon RX 570'),
        ('AMD Radeon RX 6700', 'AMD Radeon RX 6700'),
        ('AMD Radeon RX 6800 XT', 'AMD Radeon RX 6800 XT'),
        ('AMD Radeon RX 6800M', 'AMD Radeon RX 6800M'),
        ('NVIDIA Quadro RTX 3000', 'NVIDIA Quadro RTX 3000'),
        ('NVIDIA Quadro RTX 6000', 'NVIDIA Quadro RTX 6000'),
        ('AMD Radeon Pro 5300M', 'AMD Radeon Pro 5300M'),
        ('AMD Radeon Pro 5600M', 'AMD Radeon Pro 5600M'),
        ('Intel Iris Xe Graphics G7', 'Intel Iris Xe Graphics G7'),
        ('AMD Radeon R7', 'AMD Radeon R7'),
        ('AMD Radeon R9', 'AMD Radeon R9'),
        ('NVIDIA GeForce GT 1030', 'NVIDIA GeForce GT 1030'),
        ('NVIDIA GeForce GT 710', 'NVIDIA GeForce GT 710'),
        ('Intel HD Graphics 620', 'Intel HD Graphics 620'),
        ('Intel HD Graphics 630', 'Intel HD Graphics 630'),
        ('AMD Radeon RX 5500M', 'AMD Radeon RX 5500M'),
        ('AMD Radeon RX 5600M', 'AMD Radeon RX 5600M')
    ])
    graphics_memory = IntegerField('Velikost grafické paměti:', validators=[NumberRange(min=0)], default=0)

    operating_system = SelectField('Operační systém *:', choices=[('Windows', 'Windows'), ('macOS', 'macOS')],
                                   validators=[Optional()])

    ssd = BooleanField('SSD Disk:', default=False)
    hdd = BooleanField('HDD Disk:', default=False)

    ssd_capacity = IntegerField('Velikost disku SSD:', validators=[InputRequired(), NumberRange(min=0)], default=0)
    hdd_capacity = IntegerField('Velikost disku HDD:', validators=[InputRequired(), NumberRange(min=0)], default=0)

    light_keyboard = BooleanField('Podsvícená klávesnice:', default=False)
    num_keyboard = BooleanField('Numerická klávesnice:', default=False)
    touch_screen = BooleanField('Dotyková obrazovka:', default=False)
    fingerprint_reader = BooleanField('Čtečka otisků prstů:', default=False)
    memory_card_reader = BooleanField('Čtečka paměťových karet:', default=False)
    usb_c_charging = BooleanField('USB-C nabíjení:', default=False)

    battery_capacity = IntegerField('Kapacita baterie:', validators=[NumberRange(min=0)], default=0)
    construction = SelectField('Konstrukce:', choices=[('celokovovy', 'celokovový'), ('plastovy', 'plastový')])

    height = DecimalField('Výška:', validators=[NumberRange(min=0, max=999999.99)], default=0)
    height_units = SelectField('Velikostní jednotka:', choices=[('cm', 'cm'), ('in', 'in'), ('mm', 'mm')],
                               validators=[Optional()])
    width = DecimalField('Šířka:', validators=[NumberRange(min=0, max=999999.99)], default=0)
    width_units = SelectField('Velikostní jednotka:', choices=[('cm', 'cm'), ('in', 'in'), ('mm', 'mm')],
                              validators=[Optional()])
    depth = DecimalField('Hloubka:', validators=[NumberRange(min=0, max=999999.99)], default=0)
    depth_units = SelectField('Velikostní jednotka:', choices=[('cm', 'cm'), ('in', 'in'), ('mm', 'mm')],
                              validators=[Optional()])
    weight = DecimalField('Váha:', validators=[NumberRange(min=0, max=999999.99)], default=0)
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

    usb_ports = IntegerField('Počet USB portů:', validators=[NumberRange(min=0)], default=0)
    hdmi_ports = IntegerField('Počet HDMI portů:', validators=[NumberRange(min=0)], default=0)
    audio_jack = BooleanField('Audio Jack:')
    usb_3_0 = BooleanField('USB 3.0:')
    usb_2_0 = BooleanField('USB 2.0:')
    cd_dvd_drive = BooleanField('CD/DVD mechanika:')

    brand_id = SelectField('Značka:', coerce=int, choices=[], validators=[Optional()])
    category_id = SelectField('Kategorie:', coerce=int, choices=[], validators=[Optional()])

    product_image = FileField('Foto *:', validators=[InputRequired(), FileAllowed(['jpg', 'png', 'jpeg', 'webp'],
                                                                                  'Images only!')])
    additional_images = MultipleFileField('Další fotky:', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'webp'],
                                                                                  'Images only!')])

    add_product_submit = SubmitField('Přidat produkt')
    edit_product_submit = SubmitField('Upravit produkt')

    def __init__(self, *args, **kwargs):
        super(NotebookForm, self).__init__(*args, **kwargs)
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