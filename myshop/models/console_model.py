""" Libor Havránek App Copyright (C)  5.6. 2023 """

from myshop import db
from myshop.models.product_model import Product


class Console(Product):
    id = db.Column(
        db.Integer, db.ForeignKey("product.id", ondelete="CASCADE"), primary_key=True
    )

    ssd_capacity = db.Column(db.Integer, nullable=True)
    hdd_capacity = db.Column(db.Integer, nullable=True)
    ssd = db.Column(db.Boolean, nullable=True, default=False)
    hdd = db.Column(db.Boolean, nullable=True, default=False)
    dvd_drive = db.Column(db.Boolean, nullable=True, default=False)

    color = db.Column(db.String(80), nullable=True)
