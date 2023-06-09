""" Libor Havránek App Copyright (C)  20.4 2023 """

from datetime import datetime

from myshop import db


class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand_name = db.Column(db.String(30), nullable=False, unique=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    date_edited = db.Column(db.DateTime)
    edited = db.Column(db.Boolean, default=False)
    products = db.relationship(
        "Product", backref=db.backref("brand", lazy=True), cascade="all, delete"
    )
