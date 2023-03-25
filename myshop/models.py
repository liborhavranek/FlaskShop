""" Libor Havránek App Copyright (C)  23.3 2023 """

from . import db
from flask_login import UserMixin


class Customer(db.Model, UserMixin):
    #  -------------------Uzivatel-------------------
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    phone_code = db.Column(db.String(50), unique=False)
    phone = db.Column(db.String(50), unique=False)
    password = db.Column(db.String(200), unique=False)
