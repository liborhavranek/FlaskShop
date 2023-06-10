""" Libor Havránek App Copyright (C)  10.6. 2023 """

from myshop import db
from myshop.models.product_model import Product


class Headset(Product):
    id = db.Column(
        db.Integer, db.ForeignKey("product.id", ondelete="CASCADE"), primary_key=True
    )

    wireless = db.Column(db.Boolean, nullable=True, default=False)
    microphone = db.Column(db.Boolean, nullable=True, default=False)
    surround_sound = db.Column(db.Boolean, nullable=True, default=False)
    color = db.Column(db.String(80), nullable=True)
