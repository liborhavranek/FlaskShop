""" Libor Havránek App Copyright (C)  16.5 2023 """

from myshop import db
from myshop.models.product_model import Product


class Notebook(Product):
    id = db.Column(db.Integer, db.ForeignKey('product.id', ondelete="CASCADE"), primary_key=True)
    display_size = db.Column(db.Float, nullable=False)
    display_resolution = db.Column(db.String(50), nullable=False)
    display_frequency = db.Column(db.Integer, nullable=True)
    display_nits = db.Column(db.Integer, nullable=True)
    display_type = db.Column(db.String(50), nullable=False)

    processor = db.Column(db.String(80), nullable=True)
    processor_cores = db.Column(db.Integer, nullable=True)

    operating_memory = db.Column(db.Integer, nullable=False)

    graphics_card = db.Column(db.String(80), nullable=True)
    graphics_memory = db.Column(db.Integer, nullable=True)

    operating_system = db.Column(db.String(50), nullable=False)

    ssd_capacity = db.Column(db.Integer, nullable=True)
    hdd_capacity = db.Column(db.Integer, nullable=True)
    ssd = db.Column(db.Boolean, nullable=True, default=False)
    hdd = db.Column(db.Boolean, nullable=True, default=False)

    light_keyboard = db.Column(db.Boolean, nullable=True, default=False)
    num_keyboard = db.Column(db.Boolean, nullable=True, default=False)
    touch_screen = db.Column(db.Boolean, nullable=True, default=False)
    fingerprint_reader = db.Column(db.Boolean, nullable=True, default=False)
    memory_card_reader = db.Column(db.Boolean, nullable=True, default=False)
    usb_c_charging = db.Column(db.Boolean, nullable=True, default=False)

    battery_capacity = db.Column(db.Integer, nullable=True)
    construction = db.Column(db.String(50), nullable=True)

    height = db.Column(db.Numeric(10, 2), nullable=True)
    height_units = db.Column(db.String(20), nullable=True)
    width = db.Column(db.Numeric(10, 2), nullable=True)
    width_units = db.Column(db.String(20), nullable=True)
    depth = db.Column(db.Numeric(10, 2), nullable=True)
    depth_units = db.Column(db.String(20), nullable=True)

    weight = db.Column(db.Numeric(10, 2), nullable=True)
    weight_units = db.Column(db.String(20), nullable=True)

    color = db.Column(db.String(80), nullable=True)

    usb_ports = db.Column(db.Integer, nullable=True)
    hdmi_ports = db.Column(db.Integer, nullable=True)
    audio_jack = db.Column(db.Boolean, nullable=True, default=False)
    usb_3_0 = db.Column(db.Boolean, nullable=True, default=False)
    usb_2_0 = db.Column(db.Boolean, nullable=True, default=False)
    cd_dvd_drive = db.Column(db.Boolean, nullable=True, default=False)
