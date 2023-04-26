""" Libor Havránek App Copyright (C)  26.4 2023 """

from myshop import db


class ProductImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_name = db.Column(db.String(150), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id', ondelete="CASCADE"), nullable=False)
