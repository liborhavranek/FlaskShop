""" Libor Havránek App Copyright (C)  20.4 2023 """

from datetime import datetime

from myshop import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(80), nullable=False, unique=True)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    discount = db.Column(db.Integer, default=0)
    stock = db.Column(db.Integer, default=0)
    sold = db.Column(db.Integer, default=0)

    description = db.Column(db.Text, nullable=False)
    subheading = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_edited = db.Column(db.DateTime)
    edited = db.Column(db.Boolean, default=False)

    visit_count = db.Column(db.Integer, default=0)

    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id', ondelete="CASCADE"), nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id', ondelete="CASCADE"), nullable=True)

    product_image = db.Column(db.String(150), nullable=True, default='image.jpg')

    images = db.relationship('ProductImage', backref='product', lazy=True)


class Mobile(Product):
    display_size = db.Column(db.Float, nullable=False)
    display_resolution = db.Column(db.String(50), nullable=False)
    operating_system = db.Column(db.String(50), nullable=False)
    operating_memory = db.Column(db.Integer, nullable=False)
    memory = db.Column(db.Integer, nullable=False)

    battery_capacity = db.Column(db.Integer, nullable=True)
    memory_card_slot = db.Column(db.Boolean, nullable=True, default=False)
    face_id = db.Column(db.Boolean, nullable=True, default=False)
    touch_screen = db.Column(db.Boolean, nullable=True, default=False)
    front_camera = db.Column(db.Integer, nullable=True)
    back_camera = db.Column(db.Integer, nullable=True)

    height = db.Column(db.Numeric(10, 2), nullable=True)
    height_units = db.Column(db.String(20), nullable=True)
    width = db.Column(db.Numeric(10, 2), nullable=True)
    width_units = db.Column(db.String(20), nullable=True)
    depth = db.Column(db.Numeric(10, 2), nullable=True)
    depth_units = db.Column(db.String(20), nullable=True)

    weight = db.Column(db.Numeric(10, 2), nullable=True)
    weight_units = db.Column(db.String(20), nullable=True)

    color = db.Column(db.String(80), nullable=True)
    convertible = db.Column(db.Boolean, nullable=True, default=False)
    wifi = db.Column(db.Boolean, nullable=True, default=False)
    bluetooth = db.Column(db.Boolean, nullable=True, default=False)
    nfc = db.Column(db.Boolean, nullable=True, default=False)
    processor = db.Column(db.String(80), nullable=True)
    processor_cores = db.Column(db.Integer, nullable=True)
    esim = db.Column(db.Boolean, nullable=True, default=False)
