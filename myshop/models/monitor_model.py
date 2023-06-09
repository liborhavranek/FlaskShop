""" Libor Havránek App Copyright (C)  8.6 2023 """

from myshop import db
from myshop.models.product_model import Product


class Monitor(Product):
    id = db.Column(db.Integer, db.ForeignKey('product.id', ondelete="CASCADE"), primary_key=True)
    display_size = db.Column(db.Float, nullable=False)
    display_resolution = db.Column(db.String(50), nullable=False)
    refresh_rate = db.Column(db.Integer, nullable=False)
    response_time = db.Column(db.Integer, nullable=False)
    aspect_ratio = db.Column(db.String(20), nullable=False)
    connectivity = db.Column(db.String(100), nullable=False)
    color_depth = db.Column(db.Integer, nullable=True)
    curvature = db.Column(db.Boolean, nullable=True, default=False)
    height = db.Column(db.Numeric(10, 2), nullable=True)
    height_units = db.Column(db.String(20), nullable=True)
    width = db.Column(db.Numeric(10, 2), nullable=True)
    width_units = db.Column(db.String(20), nullable=True)
    depth = db.Column(db.Numeric(10, 2), nullable=True)
    depth_units = db.Column(db.String(20), nullable=True)
    weight = db.Column(db.Numeric(10, 2), nullable=True)
    weight_units = db.Column(db.String(20), nullable=True)
    color = db.Column(db.String(80), nullable=True)
    adjustable_stand = db.Column(db.Boolean, nullable=True, default=False)
    wall_mountable = db.Column(db.Boolean, nullable=True, default=False)
    built_in_speakers = db.Column(db.Boolean, nullable=True, default=False)
    energy_efficiency = db.Column(db.String(20), nullable=True)
