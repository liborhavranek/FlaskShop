""" Libor Havránek App Copyright (C)  26.4 2023 """

import unittest
from myshop import create_app, db
from myshop.models.images_model import ProductImage
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

    def create_image(self):
        self.image = ProductImage()
        self.image.image_name = "product_image_000221.jpg"
        self.image.product_id = 1
        db.session.add(self.image)
        db.session.commit()

    def test_image_have_image_name(self):
        self.create_image()
        result = ProductImage.query.filter_by(id=1).first()
        self.assertEqual(result.image_name, "product_image_000221.jpg")

    def test_image_have_product_id(self):
        self.create_image()
        result = ProductImage.query.filter_by(id=1).first()
        self.assertEqual(result.product_id, 1)
