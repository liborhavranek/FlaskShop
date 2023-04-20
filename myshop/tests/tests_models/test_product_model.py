""" Libor Havránek App Copyright (C)  20.4 2023 """

import unittest
from _decimal import Decimal
from datetime import datetime

from myshop import create_app, db
from myshop.models.product_model import Product
from myshop.tests.my_test_mixin import TestMixin


class TestCustomerAddModel(TestMixin, unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_name = cls.__name__

    def setUp(self):
        self.app = create_app(config={'TESTING': True})
        self.app.testing = True
        self.client = self.app.test_client()
        app_context = self.app.app_context()
        app_context.push()
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app.secret_key = 'test_secret_key'
        super().setUp()

    def create_product(self):
        self.product = Product()
        self.product.product_name = 'Iphone 13 Pro Max'
        self.product.price = 99.9
        self.product.description = "iPhone 13 Pro Max: Powerful flagship with 120Hz ProMotion display, " \
                                   "5G, A15 Bionic chip, and stunning camera capabilities."
        self.product.size = 23.33
        self.product.size_unit = 'cm'
        self.product.weight = 1.23
        self.product.weight_units = 'kg'
        self.product.color = 'Vesmírně šedá'
        db.session.add(self.product)
        db.session.commit()

    def test_product_have_product_name(self):
        self.create_product()
        result = Product.query.filter_by(id=1).first()
        self.assertEqual(result.product_name, 'Iphone 13 Pro Max')

    def test_product_have_price(self):
        self.create_product()
        result = Product.query.filter_by(id=1).first()
        self.assertEqual(result.price, Decimal('99.90'))

    def test_product_have_discount(self):
        self.create_product()
        result = Product.query.filter_by(id=1).first()
        self.assertEqual(result.discount, 0)

    def test_product_have_stock(self):
        self.create_product()
        result = Product.query.filter_by(id=1).first()
        self.assertEqual(result.stock, 0)

    def test_product_have_sold(self):
        self.create_product()
        result = Product.query.filter_by(id=1).first()
        self.assertEqual(result.sold, 0)

    def test_product_have_size(self):
        self.create_product()
        result = Product.query.filter_by(id=1).first()
        self.assertEqual(result.size, Decimal('23.33'))

    def test_product_have_size_unit(self):
        self.create_product()
        result = Product.query.filter_by(id=1).first()
        self.assertEqual(result.size_unit, 'cm')

    def test_product_have_weight(self):
        self.create_product()
        result = Product.query.filter_by(id=1).first()
        self.assertEqual(result.weight, Decimal('1.23'))

    def test_product_have_weight_units(self):
        self.create_product()
        result = Product.query.filter_by(id=1).first()
        self.assertEqual(result.weight_units, 'kg')

    def test_product_have_size_color(self):
        self.create_product()
        result = Product.query.filter_by(id=1).first()
        self.assertEqual(result.color, 'Vesmírně šedá')

    def test_brand_have_date_created(self):
        self.create_product()
        result = Product.query.filter_by(id=1).first()
        self.assertTrue(isinstance(result.date_created, datetime))
