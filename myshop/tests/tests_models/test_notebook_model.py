""" Libor Havránek App Copyright (C)  16.5 2023 """

import unittest
from _decimal import Decimal


from myshop import create_app, db
from myshop.models.notebook_model import Notebook

from myshop.tests.my_test_mixin import TestMixin


class TestMobileModel(TestMixin, unittest.TestCase):
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

    def create_product(self):
        self.product = Notebook()
        self.product.product_name = "Notebook Model X"
        self.product.price = 999.9
        self.product.discount = 10
        self.product.stock = 100
        self.product.description = (
            "Notebook Model X: Powerful and sleek notebook with high-resolution display, "
            "fast processor, and ample storage."
        )
        self.product.subheading = "Notebook Model X: Powerful and sleek"

        self.product.display_size = 15.6
        self.product.display_resolution = "1920 x 1080"
        self.product.display_frequency = 144
        self.product.display_nits = 300
        self.product.display_type = "IPS"

        self.product.processor = "Intel Core i7"
        self.product.processor_cores = 6

        self.product.operating_memory = 16

        self.product.graphics_card = "NVIDIA GeForce GTX 1660 Ti"
        self.product.graphics_memory = 6

        self.product.operating_system = "Windows 10"

        self.product.ssd_capacity = 512
        self.product.hdd_capacity = 1_000
        self.product.ssd = True
        self.product.hdd = True

        self.product.light_keyboard = True
        self.product.num_keyboard = True
        self.product.touch_screen = False
        self.product.fingerprint_reader = True
        self.product.memory_card_reader = True
        self.product.usb_c_charging = True

        self.product.battery_capacity = 60

        self.product.height = 19.9
        self.product.height_units = "mm"
        self.product.width = 360.4
        self.product.width_units = "mm"
        self.product.depth = 252.5
        self.product.depth_units = "mm"

        self.product.weight = 1.8
        self.product.weight_units = "kg"

        self.product.color = "Silver"

        self.product.usb_ports = 4
        self.product.hdmi_ports = 1
        self.product.audio_jack = True
        self.product.usb_3_0 = True
        self.product.usb_2_0 = True
        self.product.cd_dvd_drive = True

        self.product.brand_id = 1
        self.product.category_id = 2
        self.product.product_image = "product_image_00002.jpg"

        db.session.add(self.product)
        db.session.commit()

    def test_product_have_product_name(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(result.product_name, "Notebook Model X")

    def test_product_have_price(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(result.price, Decimal("999.90"))

    def test_product_have_discount(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(result.discount, 10)

    def test_product_have_stock(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(result.stock, 100)

    def test_product_have_sold(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(result.sold, 0)

    def test_product_have_description(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(
            result.description,
            "Notebook Model X: Powerful and sleek notebook with high-resolution display, "
            "fast processor, and ample storage.",
        )

    def test_product_have_subheading(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(result.subheading, "Notebook Model X: Powerful and sleek")

    def test_product_have_date_created(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertIsNotNone(result.date_created)

    def test_product_have_date_edited(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertIsNone(result.date_edited)

    def test_product_have_edited(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertFalse(result.edited)

    def test_product_have_visit_count(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(result.visit_count, 0)

    def test_product_have_brand_id(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(result.brand_id, 1)

    def test_product_have_category_id(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(result.category_id, 2)

    def test_product_have_product_image(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(result.product_image, "product_image_00002.jpg")

    def test_product_have_images(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(len(result.images), 0)

    def test_product_have_display_size(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(result.display_size, 15.6)

    def test_product_have_display_resolution(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(result.display_resolution, "1920 x 1080")

    def test_product_have_display_frequency(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(result.display_frequency, 144)

    def test_product_have_display_nits(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(result.display_nits, 300)

    def test_product_have_display_type(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(result.display_type, "IPS")

    def test_product_have_processor(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(result.processor, "Intel Core i7")

    def test_product_have_processor_cores(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(result.processor_cores, 6)

    def test_product_have_operating_memory(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(result.operating_memory, 16)

    def test_product_have_graphics_card(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(result.graphics_card, "NVIDIA GeForce GTX 1660 Ti")

    def test_product_have_graphics_memory(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(result.graphics_memory, 6)

    def test_product_have_operating_system(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(result.operating_system, "Windows 10")

    def test_product_have_ssd_capacity(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(result.ssd_capacity, 512)

    def test_product_have_hdd_capacity(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(result.hdd_capacity, 1000)

    def test_product_have_ssd(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertTrue(result.ssd)

    def test_product_have_hdd(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertTrue(result.hdd)

    def test_product_have_light_keyboard(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertTrue(result.light_keyboard)

    def test_product_have_num_keyboard(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertTrue(result.num_keyboard)

    def test_product_have_touch_screen(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertFalse(result.touch_screen)

    def test_product_have_fingerprint_reader(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertTrue(result.fingerprint_reader)

    def test_product_have_memory_card_reader(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertTrue(result.memory_card_reader)

    def test_product_have_usb_c_charging(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertTrue(result.usb_c_charging)

    def test_product_have_battery_capacity(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(result.battery_capacity, 60)

    def test_product_have_construction(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertIsNone(result.construction)

    def test_product_have_height(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(result.height, Decimal("19.90"))

    def test_product_have_height_units(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(result.height_units, "mm")

    def test_product_have_width(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(result.width, Decimal("360.40"))

    def test_product_have_width_units(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(result.width_units, "mm")

    def test_product_have_depth(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(result.depth, Decimal("252.50"))

    def test_product_have_depth_units(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(result.depth_units, "mm")

    def test_product_have_weight(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(result.weight, Decimal("1.80"))

    def test_product_have_weight_units(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(result.weight_units, "kg")

    def test_product_have_color(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(result.color, "Silver")

    def test_product_have_usb_ports(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(result.usb_ports, 4)

    def test_product_have_hdmi_ports(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertEqual(result.hdmi_ports, 1)

    def test_product_have_audio_jack(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertTrue(result.audio_jack)

    def test_product_have_usb_3_0(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertTrue(result.usb_3_0)

    def test_product_have_usb_2_0(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertTrue(result.usb_2_0)

    def test_product_have_cd_dvd_drive(self):
        self.create_product()
        result = Notebook.query.filter_by(id=1).first()
        self.assertTrue(result.cd_dvd_drive)
