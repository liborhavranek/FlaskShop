""" Libor Havránek App Copyright (C)  6.6 2023 """

from myshop import db


class Wishlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id', ondelete="CASCADE"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id', ondelete="CASCADE"), nullable=False)
