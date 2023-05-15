""" Libor Havránek App Copyright (C)  21.4 2023 """

import unittest

from myshop import create_app
from myshop.forms.add_mobile_form import MobileForm
from myshop.tests.my_test_mixin import TestMixin


class TestMobileForm(TestMixin, unittest.TestCase):
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
        self.form = MobileForm()
        super().setUp()

    def test_product_form_have_csrf_token_field(self):
        self.assertIn('csrf_token', self.form._fields)

    def test_product_form_have_product_name_field(self):
        self.assertIn('product_name', self.form._fields)

    def test_product_form_have_price_field(self):
        self.assertIn('price', self.form._fields)

    def test_product_form_have_discount_field(self):
        self.assertIn('discount', self.form._fields)

    def test_product_form_have_stock_field(self):
        self.assertIn('stock', self.form._fields)

    def test_product_form_have_subheading_field(self):
        self.assertIn('subheading', self.form._fields)

    def test_product_form_have_description_field(self):
        self.assertIn('description', self.form._fields)

    def test_product_form_have_size_field(self):
        self.assertIn('display_size', self.form._fields)

    def test_product_form_have_size_units_field(self):
        self.assertIn('display_resolution', self.form._fields)

    def test_product_form_have_operating_system_field(self):
        self.assertIn('operating_system', self.form._fields)

    def test_product_form_have_operating_memory_field(self):
        self.assertIn('operating_memory', self.form._fields)

    def test_product_form_have_memory_field(self):
        self.assertIn('memory', self.form._fields)

    def test_product_form_have_battery_capacity_field(self):
        self.assertIn('battery_capacity', self.form._fields)

    def test_product_form_have_memory_card_slot_field(self):
        self.assertIn('memory_card_slot', self.form._fields)

    def test_product_form_have_face_id_field(self):
        self.assertIn('face_id', self.form._fields)

    def test_product_form_have_touch_screen_field(self):
        self.assertIn('touch_screen', self.form._fields)

    def test_product_form_have_front_camera_field(self):
        self.assertIn('front_camera', self.form._fields)

    def test_product_form_have_back_camera_field(self):
        self.assertIn('back_camera', self.form._fields)

    def test_product_form_have_height_field(self):
        self.assertIn('height', self.form._fields)

    def test_product_form_have_height_units_field(self):
        self.assertIn('height_units', self.form._fields)

    def test_product_form_have_width_field(self):
        self.assertIn('width', self.form._fields)

    def test_product_form_have_width_units_field(self):
        self.assertIn('width_units', self.form._fields)

    def test_product_form_have_depth_field(self):
        self.assertIn('depth', self.form._fields)

    def test_product_form_have_depth_units_field(self):
        self.assertIn('depth_units', self.form._fields)

    def test_product_form_have_weight_field(self):
        self.assertIn('weight', self.form._fields)

    def test_product_form_have_weight_units_field(self):
        self.assertIn('weight_units', self.form._fields)

    def test_product_form_have_color_field(self):
        self.assertIn('color', self.form._fields)

    def test_product_form_have_convertible_field(self):
        self.assertIn('convertible', self.form._fields)

    def test_product_form_have_wifi_field(self):
        self.assertIn('wifi', self.form._fields)

    def test_product_form_have_bluetooth_field(self):
        self.assertIn('bluetooth', self.form._fields)

    def test_product_form_have_nfc_field(self):
        self.assertIn('nfc', self.form._fields)

    def test_product_form_have_processor_field(self):
        self.assertIn('processor', self.form._fields)

    def test_product_form_have_processor_cores_field(self):
        self.assertIn('processor_cores', self.form._fields)

    def test_product_form_have_esim_field(self):
        self.assertIn('esim', self.form._fields)

    def test_product_form_have_brand_id_field(self):
        self.assertIn('brand_id', self.form._fields)

    def test_product_form_have_category_id_field(self):
        self.assertIn('category_id', self.form._fields)

    def test_product_form_have_add_product_submit_field(self):
        self.assertIn('add_product_submit', self.form._fields)

    def test_product_form_have_edit_product_submit_field(self):
        self.assertIn('edit_product_submit', self.form._fields)

    def test_product_form_have_product_image(self):
        self.assertIn('product_image', self.form._fields)

    def test_product_form_have_additional_images(self):
        self.assertIn('additional_images', self.form._fields)

    def test_product_form_have_product_name_label(self):
        field = self.form._fields['product_name']
        self.assertEqual(field.label.text, 'Název *:')

    def test_price_label(self):
        field = self.form._fields['price']
        self.assertEqual(field.label.text, 'Cena *:')

    def test_discount_label(self):
        field = self.form._fields['discount']
        self.assertEqual(field.label.text, 'Sleva:')

    def test_stock_label(self):
        field = self.form._fields['stock']
        self.assertEqual(field.label.text, 'Počet kusů:')

    def test_subheading_label(self):
        field = self.form._fields['subheading']
        self.assertEqual(field.label.text, 'Podnadpis *:')

    def test_description_label(self):
        field = self.form._fields['description']
        self.assertEqual(field.label.text, 'Popis *:')

    def test_display_size_label(self):
        field = self.form._fields['display_size']
        self.assertEqual(field.label.text, 'Velikost displeje *:')

    def test_display_resolution_label(self):
        field = self.form._fields['display_resolution']
        self.assertEqual(field.label.text, 'Rozlišení displeje *:')

    def test_operating_system_label(self):
        field = self.form._fields['operating_system']
        self.assertEqual(field.label.text, 'Operační systém *:')

    def test_operating_memory_label(self):
        field = self.form._fields['operating_memory']
        self.assertEqual(field.label.text, 'Operační paměť *:')

    def test_memory_label(self):
        field = self.form._fields['memory']
        self.assertEqual(field.label.text, 'Velikost disku *:')

    def test_battery_capacity_label(self):
        field = self.form._fields['battery_capacity']
        self.assertEqual(field.label.text, 'Kapacita baterie:')

    def test_memory_card_slot_label(self):
        field = self.form._fields['memory_card_slot']
        self.assertEqual(field.label.text, 'Slot na paměťovou kartu:')

    def test_face_id_label(self):
        field = self.form._fields['face_id']
        self.assertEqual(field.label.text, 'Face ID:')

    def test_touch_screen_label(self):
        field = self.form._fields['touch_screen']
        self.assertEqual(field.label.text, 'Dotyková obrazovka:')

    def test_front_camera_label(self):
        field = self.form._fields['front_camera']
        self.assertEqual(field.label.text, 'Přední kamera:')

    def test_back_camera_label(self):
        field = self.form._fields['back_camera']
        self.assertEqual(field.label.text, 'Zadní kamera:')

    def test_height_label(self):
        field = self.form._fields['height']
        self.assertEqual(field.label.text, 'Výška:')

    def test_height_units_label(self):
        field = self.form._fields['height_units']
        self.assertEqual(field.label.text, 'Velikostní jednotka:')

    def test_width_label(self):
        field = self.form._fields['width']
        self.assertEqual(field.label.text, 'Šířka:')

    def test_width_units_label(self):
        field = self.form._fields['width_units']
        self.assertEqual(field.label.text, 'Velikostní jednotka:')

    def test_depth_label(self):
        field = self.form._fields['depth']
        self.assertEqual(field.label.text, 'Hloubka:')

    def test_depth_units_label(self):
        field = self.form._fields['depth_units']
        self.assertEqual(field.label.text, 'Velikostní jednotka:')

    def test_weight_label(self):
        field = self.form._fields['weight']
        self.assertEqual(field.label.text, 'Váha:')

    def test_weight_units_label(self):
        field = self.form._fields['weight_units']
        self.assertEqual(field.label.text, 'Váhová jednotka:')

    def test_color_label(self):
        field = self.form._fields['color']
        self.assertEqual(field.label.text, 'Barva:')

    def test_convertible_label(self):
        field = self.form._fields['convertible']
        self.assertEqual(field.label.text, 'Ohebný:')

    def test_wifi_label(self):
        field = self.form._fields['wifi']
        self.assertEqual(field.label.text, 'WiFi:')

    def test_bluetooth_label(self):
        field = self.form._fields['bluetooth']
        self.assertEqual(field.label.text, 'Bluetooth:')

    def test_nfc_label(self):
        field = self.form._fields['nfc']
        self.assertEqual(field.label.text, 'NFC:')

    def test_processor_label(self):
        field = self.form._fields['processor']
        self.assertEqual(field.label.text, 'Procesor:')

    def test_processor_cores_label(self):
        field = self.form._fields['processor_cores']
        self.assertEqual(field.label.text, 'Počet jader:')

    def test_esim_label(self):
        field = self.form._fields['esim']
        self.assertEqual(field.label.text, 'eSIM:')

    def test_brand_id_label(self):
        field = self.form._fields['brand_id']
        self.assertEqual(field.label.text, 'Značka:')

    def test_product_image_label(self):
        field = self.form._fields['product_image']
        self.assertEqual(field.label.text, 'Foto *:')

    def test_additional_images_label(self):
        field = self.form._fields['additional_images']
        self.assertEqual(field.label.text, 'Další fotky:')

    def test_add_product_submit_label(self):
        field = self.form._fields['add_product_submit']
        self.assertEqual(field.label.text, 'Přidat produkt')

    def test_edit_product_submit_label(self):
        field = self.form._fields['edit_product_submit']
        self.assertEqual(field.label.text, 'Upravit produkt')
