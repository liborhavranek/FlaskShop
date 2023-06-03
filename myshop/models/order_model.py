""" Libor Havránek App Copyright (C)  2.6 2023 """

from datetime import datetime
from myshop import db


class CustomerOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    customer = db.relationship('Customer', backref=db.backref('orders', lazy=True))
    customer_first_name = db.Column(db.String(50), nullable=False)
    customer_last_name = db.Column(db.String(50), nullable=False)
    customer_email = db.Column(db.String(50), nullable=False)
    customer_phone_code = db.Column(db.String(50), nullable=False)
    customer_phone = db.Column(db.String(50), nullable=False)

    customer_city = db.Column(db.String(50), unique=False, nullable=False)
    customer_street = db.Column(db.String(50), unique=False, nullable=False)
    customer_zipcode = db.Column(db.String(50), unique=False, nullable=False)
    customer_info = db.Column(db.String(50), unique=False, nullable=True)

    products = db.relationship('Product', secondary='order_products', backref=db.backref('orders', lazy=True))
    total_price = db.Column(db.Numeric(10, 2), nullable=False)
    payment_status = db.Column(db.Boolean, nullable=False, default=False)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, customer, customer_name, customer_email, customer_phone_code, customer_phone, products,
                 total_price, payment_status, customer_city, customer_street, customer_zipcode, customer_info):
        self.customer = customer
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.customer_phone_code = customer_phone_code
        self.customer_phone = customer_phone

        self.customer_city = customer_city
        self.customer_street = customer_street
        self.customer_zipcode = customer_zipcode
        self.customer_info = customer_info

        self.products = products
        self.total_price = total_price
        self.payment_status = payment_status
