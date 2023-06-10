""" Libor Havránek App Copyright (C)  20.4 2023 """

import unittest
from datetime import datetime
from myshop import create_app, db
from myshop.models.category_model import Category
from myshop.tests.my_test_mixin import TestMixin


class TestCustomerAddModel(TestMixin, unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_name = cls.__name__

    def setUp(self):
        self.app = create_app(config={"TESTING": True})
        self.app.testing = True
        self.client = self.app.test_client()
        app_context = self.app.app_context()
        app_context.push()
        self.app.config["TESTING"] = True
        self.app.config["WTF_CSRF_ENABLED"] = False
        self.app.secret_key = "test_secret_key"
        super().setUp()

    def create_category(self):
        self.category = Category()
        self.category.category_name = "Apple"
        db.session.add(self.category)
        db.session.commit()

    def test_brand_have_brand_name(self):
        self.create_category()
        result = Category.query.filter_by(id=1).first()
        self.assertEqual(result.category_name, "Apple")

    def test_brand_have_date_created(self):
        self.create_category()
        result = Category.query.filter_by(id=1).first()
        self.assertTrue(isinstance(result.date_created, datetime))

    def test_brand_have_edited(self):
        self.create_category()
        result = Category.query.filter_by(id=1).first()
        self.assertFalse(result.edited)
