""" Libor Havránek App Copyright (C)  16.5 2023 """

from myshop import db
from myshop.models.product_model import Product


class Mobile(Product):
    id = db.Column(db.Integer, db.ForeignKey('product.id', ondelete="CASCADE"), primary_key=True)
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
