""" Libor Havránek App Copyright (C)  2.6 2023 """

from datetime import datetime
from myshop import db


class CustomerOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=True)
    customer_first_name = db.Column(db.String(50), nullable=False)
    customer_last_name = db.Column(db.String(50), nullable=False)
    customer_email = db.Column(db.String(50), nullable=False)
    customer_phone_code = db.Column(db.String(50), nullable=False)
    customer_phone = db.Column(db.String(50), nullable=False)
    customer_city = db.Column(db.String(50), unique=False, nullable=False)
    customer_street = db.Column(db.String(50), unique=False, nullable=False)
    customer_zipcode = db.Column(db.String(50), unique=False, nullable=False)
    customer_info = db.Column(db.String(50), unique=False, nullable=True)

    payment_status = db.Column(db.Boolean, nullable=False, default=False)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    total_price = db.Column(db.Float, nullable=False)

    customer = db.relationship('Customer', backref='orders')

    products = db.Column(db.String(5000), nullable=False, default="[]")  # Storing products as JSON
