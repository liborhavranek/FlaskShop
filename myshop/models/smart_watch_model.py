""" Libor Havránek App Copyright (C)  6.6 2023 """

from myshop import db
from myshop.models.product_model import Product


class SmartWatch(Product):
    id = db.Column(db.Integer, db.ForeignKey('product.id', ondelete="CASCADE"), primary_key=True)
    display_size = db.Column(db.Float, nullable=False)
    display_resolution = db.Column(db.String(50), nullable=False)

    operating_system = db.Column(db.String(50), nullable=False)
    memory = db.Column(db.Integer, nullable=False)

    battery_capacity = db.Column(db.Integer, nullable=True)

    weight = db.Column(db.Numeric(10, 2), nullable=True)
    weight_units = db.Column(db.String(20), nullable=True)

    color = db.Column(db.String(80), nullable=True)

    bluetooth = db.Column(db.Boolean, nullable=True, default=False)
    wifi = db.Column(db.Boolean, nullable=True, default=False)
    nfc = db.Column(db.Boolean, nullable=True, default=False)
    esim = db.Column(db.Boolean, nullable=True, default=False)

    heart_rate_monitor = db.Column(db.Boolean, nullable=True, default=False)
    step_counter = db.Column(db.Boolean, nullable=True, default=False)
    sleep_tracker = db.Column(db.Boolean, nullable=True, default=False)
    gps = db.Column(db.Boolean, nullable=True, default=False)
    water_resistant = db.Column(db.Boolean, nullable=True, default=False)
    music_player = db.Column(db.Boolean, nullable=True, default=False)
    voice_assistant = db.Column(db.Boolean, nullable=True, default=False)
