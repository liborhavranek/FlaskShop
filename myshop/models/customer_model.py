""" Libor Havránek App Copyright (C)  23.3 2023 """

from myshop import db
from flask_login import UserMixin


class Customer(db.Model, UserMixin):
    #  -------------------Uzivatel-------------------
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    phone_code = db.Column(db.String(50), unique=False)
    phone = db.Column(db.String(50), unique=False)
    user_password = db.Column(db.String(200), unique=False)

    # --------------- Fakturacni udaje ---------------------
    faktura_first_name = db.Column(db.String(50), unique=False, nullable=True)
    faktura_last_name = db.Column(db.String(50), unique=False, nullable=True)
    faktura_city = db.Column(db.String(50), unique=False, nullable=True)
    faktura_street = db.Column(db.String(50), unique=False, nullable=True)
    faktura_zipcode = db.Column(db.String(50), unique=False, nullable=True)

    # ---------------Dodaci udaje ---------------------------------

    dodej_first_name = db.Column(db.String(50), unique=False, nullable=True)
    dodej_last_name = db.Column(db.String(50), unique=False, nullable=True)
    dodej_company = db.Column(db.String(50), unique=False, nullable=True)
    dodej_city = db.Column(db.String(50), unique=False, nullable=True)
    dodej_street = db.Column(db.String(50), unique=False, nullable=True)
    dodej_zipcode = db.Column(db.String(50), unique=False, nullable=True)
    dodej_info = db.Column(db.String(50), unique=False, nullable=True)
    dodej_phone_code = db.Column(db.String(50), unique=False, nullable=True)
    dodej_phone = db.Column(db.String(50), unique=False, nullable=True)

    # -------------------Firemní údaje -------------------------------------

    firma_ico = db.Column(db.String(50), unique=False, nullable=True)
    firma_dic = db.Column(db.String(50), unique=False, nullable=True)
    firma_bank_acc = db.Column(db.String(50), unique=False, nullable=True)
    firma_bank_number = db.Column(db.String(50), unique=False, nullable=True)
    firma_spec_symbol = db.Column(db.String(50), unique=False, nullable=True)

    wishlist = db.relationship("Wishlist", backref="customer", lazy=True)

    role = db.Column(db.String(20), default="user")
