""" Libor Havránek App Copyright (C)  20.4 2023 """

import unittest
from _decimal import Decimal


from myshop import create_app, db
from myshop.models.mobile_model import Mobile

from myshop.tests.my_test_mixin import TestMixin


class TestMobileModel(TestMixin, unittest.TestCase):
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
        self.product = Mobile()
        self.product.product_name = 'Iphone 13 Pro Max'
        self.product.price = 99.9
        self.product.discount = 0
        self.product.stock = 0
        self.product.description = "iPhone 13 Pro Max: Powerful flagship with 120Hz ProMotion display, " \
                                   "5G, A15 Bionic chip, and stunning camera capabilities."
        self.product.subheading = "iPhone 13 Pro Max: Powerful flagship"

        self.product.display_size = 7.8
        self.product.display_resolution = '1200 x 1200'
        self.product.operating_system = 'Android'
        self.product.operating_memory = 12
        self.product.memory = 12

        self.product.battery_capacity = 4000
        self.product.memory_card_slot = False
        self.product.face_id = True
        self.product.touch_screen = True
        self.product.front_camera = 12
        self.product.back_camera = 12

        self.product.height = 11.2
        self.product.height_units = 'mm'
        self.product.weight = 1.23
        self.product.weight_units = 'kg'
        self.product.depth = 11.8
        self.product.depth_units = 'mm'
        self.product.color = 'cerna'
        self.product.convertible = False
        self.product.wifi = True
        self.product.bluetooth = True
        self.product.nfc = True
        self.product.processor = 'Apple A14 Bionic'
        self.product.processor_cores = 8
        self.product.brand_id = 1
        self.product.category_id = 1
        self.product.product_image = 'product_image_00001.jpg'
        db.session.add(self.product)
        db.session.commit()

    def test_product_have_product_name(self):
        self.create_product()
        result = Mobile.query.filter_by(id=1).first()
        self.assertEqual(result.product_name, 'Iphone 13 Pro Max')

    def test_product_have_price(self):
        self.create_product()
        result = Mobile.query.filter_by(id=1).first()
        self.assertEqual(result.price, Decimal('99.90'))

    def test_product_have_discount(self):
        self.create_product()
        result = Mobile.query.filter_by(id=1).first()
        self.assertEqual(result.discount, 0)

    def test_product_have_stock(self):
        self.create_product()
        result = Mobile.query.filter_by(id=1).first()
        self.assertEqual(result.stock, 0)

    def test_product_have_description(self):
        self.create_product()
        result = Mobile.query.filter_by(id=1).first()
        self.assertEqual(result.description,
                         "iPhone 13 Pro Max: Powerful flagship with 120Hz ProMotion display, 5G,"
                         " A15 Bionic chip, and stunning camera capabilities.")

    def test_product_have_subheading(self):
        self.create_product()
        result = Mobile.query.filter_by(id=1).first()
        self.assertEqual(result.subheading, "iPhone 13 Pro Max: Powerful flagship")

    def test_product_have_display_size(self):
        self.create_product()
        result = Mobile.query.filter_by(id=1).first()
        self.assertEqual(result.display_size, 7.8)

    def test_product_have_display_resolution(self):
        self.create_product()
        result = Mobile.query.filter_by(id=1).first()
        self.assertEqual(result.display_resolution, '1200 x 1200')

    def test_product_have_operating_system(self):
        self.create_product()
        result = Mobile.query.filter_by(id=1).first()
        self.assertEqual(result.operating_system, 'Android')

    def test_product_have_operating_memory(self):
        self.create_product()
        result = Mobile.query.filter_by(id=1).first()
        self.assertEqual(result.operating_memory, 12)

    def test_product_have_memory(self):
        self.create_product()
        result = Mobile.query.filter_by(id=1).first()
        self.assertEqual(result.memory, 12)

    def test_product_have_battery_capacity(self):
        self.create_product()
        result = Mobile.query.filter_by(id=1).first()
        self.assertEqual(result.battery_capacity, 4000)

    def test_product_have_memory_card_slot(self):
        self.create_product()
        result = Mobile.query.filter_by(id=1).first()
        self.assertEqual(result.memory_card_slot, False)

    def test_product_have_face_id(self):
        self.create_product()
        result = Mobile.query.filter_by(id=1).first()
        self.assertEqual(result.face_id, True)

    def test_product_have_touch_screen(self):
        self.create_product()
        result = Mobile.query.filter_by(id=1).first()
        self.assertEqual(result.touch_screen, True)

    def test_product_have_front_camera(self):
        self.create_product()
        result = Mobile.query.filter_by(id=1).first()
        self.assertEqual(result.front_camera, 12)

    def test_product_have_back_camera(self):
        self.create_product()
        result = Mobile.query.filter_by(id=1).first()
        self.assertEqual(result.back_camera, 12)

    def test_product_have_height(self):
        self.create_product()
        result = Mobile.query.filter_by(id=1).first()
        self.assertEqual(result.height, Decimal('11.20'))

    def test_product_have_height_units(self):
        self.create_product()
        result = Mobile.query.filter_by(id=1).first()
        self.assertEqual(result.height_units, 'mm')

    def test_product_have_weight(self):
        self.create_product()
        result = Mobile.query.filter_by(id=1).first()
        self.assertEqual(result.weight, Decimal('1.23'))

    def test_product_have_weight_units(self):
        self.create_product()
        result = Mobile.query.filter_by(id=1).first()
        self.assertEqual(result.weight_units, 'kg')

    def test_product_have_depth(self):
        self.create_product()
        result = Mobile.query.filter_by(id=1).first()
        self.assertEqual(result.depth, Decimal('11.80'))

    def test_product_have_depth_units(self):
        self.create_product()
        result = Mobile.query.filter_by(id=1).first()
        self.assertEqual(result.depth_units, 'mm')

    def test_product_have_color(self):
        self.create_product()
        result = Mobile.query.filter_by(id=1).first()
        self.assertEqual(result.color, 'cerna')

    def test_product_have_convertible(self):
        self.create_product()
        result = Mobile.query.filter_by(id=1).first()
        self.assertEqual(result.convertible, False)

    def test_product_have_wifi(self):
        self.create_product()
        result = Mobile.query.filter_by(id=1).first()
        self.assertEqual(result.wifi, True)

    def test_product_have_bluetooth(self):
        self.create_product()
        result = Mobile.query.filter_by(id=1).first()
        self.assertEqual(result.bluetooth, True)

    def test_product_have_nfc(self):
        self.create_product()
        result = Mobile.query.filter_by(id=1).first()
        self.assertEqual(result.nfc, True)

    def test_product_have_processor(self):
        self.create_product()
        result = Mobile.query.filter_by(id=1).first()
        self.assertEqual(result.processor, 'Apple A14 Bionic')

    def test_product_have_processor_cores(self):
        self.create_product()
        result = Mobile.query.filter_by(id=1).first()
        self.assertEqual(result.processor_cores, 8)

    def test_product_have_brand_id(self):
        self.create_product()
        result = Mobile.query.filter_by(id=1).first()
        self.assertEqual(result.brand_id, 1)

    def test_product_have_category_id(self):
        self.create_product()
        result = Mobile.query.filter_by(id=1).first()
        self.assertEqual(result.category_id, 1)
