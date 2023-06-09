""" Libor Havránek App Copyright (C)  8.6 2023 """

import unittest

from myshop import create_app, db
from myshop.models.customer_model import Customer
from myshop.models.product_model import Product
from myshop.models.wish_list_model import Wishlist

from myshop.tests.my_test_mixin import TestMixin


class TestWishlistModel(TestMixin, unittest.TestCase):
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

    def create_wishlist(self):
        self.customer = Customer()
        self.customer.first_name = "John"
        self.customer.last_name = "Doe"
        # Set other customer attributes as needed
        db.session.add(self.customer)
        db.session.commit()

        self.product = Product()
        self.product.product_name = "Play station 4"
        self.product.price = 999.9
        self.product.discount = 10
        self.product.stock = 100
        self.product.description = (
            "Play station 4: Powerful and sleek console with high-resolution display, "
            "fast processor, and ample storage."
        )
        self.product.subheading = "Play station 4: Powerful and sleek"

        self.product.ssd_capacity = 512
        self.product.hdd_capacity = 1_000
        self.product.ssd = True
        self.product.hdd = True

        self.product.dvd_drive = True

        self.product.color = "Silver"

        self.product.brand_id = 1
        self.product.category_id = 2
        self.product.product_image = "product_image_00002.jpg"
        db.session.add(self.product)
        db.session.commit()

        self.wishlist = Wishlist()
        self.wishlist.customer_id = self.customer.id
        self.wishlist.product_id = self.product.id
        db.session.add(self.wishlist)
        db.session.commit()

    def test_wishlist_has_customer_id(self):
        self.create_wishlist()
        result = Wishlist.query.filter_by(id=1).first()
        self.assertEqual(result.customer_id, self.customer.id)

    def test_wishlist_has_product_id(self):
        self.create_wishlist()
        result = Wishlist.query.filter_by(id=1).first()
        self.assertEqual(result.product_id, self.product.id)
