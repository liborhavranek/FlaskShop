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
    size = db.Column(db.Numeric(10, 2), nullable=True)
    size_units = db.Column(db.String(20), nullable=True)
    weight = db.Column(db.Numeric(10, 2), nullable=True)
    weight_units = db.Column(db.String(20), nullable=True)
    color = db.Column(db.String(80), nullable=True)
    description = db.Column(db.Text, nullable=False)
    subheading = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_edited = db.Column(db.DateTime)
    edited = db.Column(db.Boolean, default=False)

    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id', ondelete="CASCADE"), nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id', ondelete="CASCADE"), nullable=True)

    product_image = db.Column(db.String(150), nullable=True, default='image.jpg')

    images = db.relationship('ProductImage', backref='product', lazy=True)
