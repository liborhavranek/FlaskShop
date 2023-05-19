""" Libor Havránek App Copyright (C)  17.5 2023 """

import unittest

from myshop import create_app
from myshop.forms.add_notebook_form import NotebookForm
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
        self.form = NotebookForm()
        super().setUp()

    def test_notebook_form_have_csrf_token_field(self):
        self.assertIn('csrf_token', self.form._fields)

    def test_notebook_form_have_product_name_field(self):
        self.assertIn('product_name', self.form._fields)

    def test_notebook_form_have_price_field(self):
        self.assertIn('price', self.form._fields)

    def test_notebook_form_have_discount_field(self):
        self.assertIn('discount', self.form._fields)

    def test_notebook_form_have_stock_field(self):
        self.assertIn('stock', self.form._fields)

    def test_notebook_form_have_description_field(self):
        self.assertIn('description', self.form._fields)

    def test_notebook_form_have_subheading_field(self):
        self.assertIn('subheading', self.form._fields)

    def test_notebook_form_have_display_size_field(self):
        self.assertIn('display_size', self.form._fields)

    def test_notebook_form_have_display_resolution_field(self):
        self.assertIn('display_resolution', self.form._fields)

    def test_notebook_form_have_display_frequency_field(self):
        self.assertIn('display_frequency', self.form._fields)

    def test_notebook_form_have_display_nits_field(self):
        self.assertIn('display_nits', self.form._fields)

    def test_notebook_form_have_display_type_field(self):
        self.assertIn('display_type', self.form._fields)

    def test_notebook_form_have_processor_field(self):
        self.assertIn('processor', self.form._fields)

    def test_notebook_form_have_processor_cores_field(self):
        self.assertIn('processor_cores', self.form._fields)

    def test_notebook_form_have_operating_memory_field(self):
        self.assertIn('operating_memory', self.form._fields)

    def test_notebook_form_have_graphics_card_field(self):
        self.assertIn('graphics_card', self.form._fields)

    def test_notebook_form_have_graphics_memory_field(self):
        self.assertIn('graphics_memory', self.form._fields)

    def test_notebook_form_have_operating_system_field(self):
        self.assertIn('operating_system', self.form._fields)

    def test_notebook_form_have_ssd_field(self):
        self.assertIn('ssd', self.form._fields)

    def test_notebook_form_have_hdd_field(self):
        self.assertIn('hdd', self.form._fields)

    def test_notebook_form_have_ssd_capacity_field(self):
        self.assertIn('ssd_capacity', self.form._fields)

    def test_notebook_form_have_hdd_capacity_field(self):
        self.assertIn('hdd_capacity', self.form._fields)

    def test_notebook_form_have_light_keyboard_field(self):
        self.assertIn('light_keyboard', self.form._fields)

    def test_notebook_form_have_num_keyboard_field(self):
        self.assertIn('num_keyboard', self.form._fields)

    def test_notebook_form_have_touch_screen_field(self):
        self.assertIn('touch_screen', self.form._fields)

    def test_notebook_form_have_fingerprint_reader_field(self):
        self.assertIn('fingerprint_reader', self.form._fields)

    def test_notebook_form_have_memory_card_reader_field(self):
        self.assertIn('memory_card_reader', self.form._fields)

    def test_notebook_form_have_usb_c_charging_field(self):
        self.assertIn('usb_c_charging', self.form._fields)

    def test_notebook_form_have_battery_capacity_field(self):
        self.assertIn('battery_capacity', self.form._fields)

    def test_notebook_form_have_height_field(self):
        self.assertIn('height', self.form._fields)

    def test_notebook_form_have_height_units_field(self):
        self.assertIn('height_units', self.form._fields)

    def test_notebook_form_have_width_field(self):
        self.assertIn('width', self.form._fields)

    def test_notebook_form_have_width_units_field(self):
        self.assertIn('width_units', self.form._fields)

    def test_notebook_form_have_depth_field(self):
        self.assertIn('depth', self.form._fields)

    def test_notebook_form_have_depth_units_field(self):
        self.assertIn('depth_units', self.form._fields)

    def test_notebook_form_have_weight_field(self):
        self.assertIn('weight', self.form._fields)

    def test_notebook_form_have_weight_units_field(self):
        self.assertIn('weight_units', self.form._fields)

    def test_notebook_form_have_color_field(self):
        self.assertIn('color', self.form._fields)

    def test_notebook_form_have_usb_ports_field(self):
        self.assertIn('usb_ports', self.form._fields)

    def test_notebook_form_have_hdmi_ports_field(self):
        self.assertIn('hdmi_ports', self.form._fields)

    def test_notebook_form_have_audio_jack_field(self):
        self.assertIn('audio_jack', self.form._fields)

    def test_notebook_form_have_usb_3_0_field(self):
        self.assertIn('usb_3_0', self.form._fields)

    def test_notebook_form_have_usb_2_0_field(self):
        self.assertIn('usb_2_0', self.form._fields)

    def test_notebook_form_have_cd_dvd_drive_field(self):
        self.assertIn('cd_dvd_drive', self.form._fields)

    def test_notebook_form_have_brand_id_field(self):
        self.assertIn('brand_id', self.form._fields)

    def test_notebook_form_have_category_id_field(self):
        self.assertIn('category_id', self.form._fields)

    def test_notebook_form_have_product_image_field(self):
        self.assertIn('product_image', self.form._fields)

    def test_notebook_form_have_additional_images_field(self):
        self.assertIn('additional_images', self.form._fields)

    def test_add_product_submit_label(self):
        field = self.form._fields['add_product_submit']
        self.assertEqual(field.label.text, 'Přidat produkt')

    def test_edit_product_submit_label(self):
        field = self.form._fields['edit_product_submit']
        self.assertEqual(field.label.text, 'Upravit produkt')

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

    def test_description_label(self):
        field = self.form._fields['description']
        self.assertEqual(field.label.text, 'Popis *:')

    def test_subheading_label(self):
        field = self.form._fields['subheading']
        self.assertEqual(field.label.text, 'Podnadpis *:')

    def test_display_size_label(self):
        field = self.form._fields['display_size']
        self.assertEqual(field.label.text, 'Velikost displeje *:')

    def test_display_resolution_label(self):
        field = self.form._fields['display_resolution']
        self.assertEqual(field.label.text, 'Rozlišení displeje *:')

    def test_display_frequency_label(self):
        field = self.form._fields['display_frequency']
        self.assertEqual(field.label.text, 'Frekvence obnovování:')

    def test_display_nits_label(self):
        field = self.form._fields['display_nits']
        self.assertEqual(field.label.text, 'Jas displeje:')

    def test_display_type_label(self):
        field = self.form._fields['display_type']
        self.assertEqual(field.label.text, 'Typ displeje:')

    def test_processor_label(self):
        field = self.form._fields['processor']
        self.assertEqual(field.label.text, 'Procesor:')

    def test_processor_cores_label(self):
        field = self.form._fields['processor_cores']
        self.assertEqual(field.label.text, 'Počet jader:')

    def test_operating_memory_label(self):
        field = self.form._fields['operating_memory']
        self.assertEqual(field.label.text, 'Operační paměť *:')

    def test_graphics_card_label(self):
        field = self.form._fields['graphics_card']
        self.assertEqual(field.label.text, 'Grafická karta:')

    def test_graphics_memory_label(self):
        field = self.form._fields['graphics_memory']
        self.assertEqual(field.label.text, 'Velikost grafické paměti:')

    def test_operating_system_label(self):
        field = self.form._fields['operating_system']
        self.assertEqual(field.label.text, 'Operační systém *:')

    def test_ssd_label(self):
        field = self.form._fields['ssd']
        self.assertEqual(field.label.text, 'SSD Disk:')

    def test_hdd_label(self):
        field = self.form._fields['hdd']
        self.assertEqual(field.label.text, 'HDD Disk:')

    def test_ssd_capacity_label(self):
        field = self.form._fields['ssd_capacity']
        self.assertEqual(field.label.text, 'Velikost disku SSD:')

    def test_hdd_capacity_label(self):
        field = self.form._fields['hdd_capacity']
        self.assertEqual(field.label.text, 'Velikost disku HDD:')

    def test_light_keyboard_label(self):
        field = self.form._fields['light_keyboard']
        self.assertEqual(field.label.text, 'Podsvícená klávesnice:')

    def test_num_keyboard_label(self):
        field = self.form._fields['num_keyboard']
        self.assertEqual(field.label.text, 'Numerická klávesnice:')

    def test_touchscreen_label(self):
        field = self.form._fields['touch_screen']
        self.assertEqual(field.label.text, 'Dotyková obrazovka:')

    def test_fingerprint_reader_label(self):
        field = self.form._fields['fingerprint_reader']
        self.assertEqual(field.label.text, 'Čtečka otisků prstů:')

    def test_memory_card_reader_label(self):
        field = self.form._fields['memory_card_reader']
        self.assertEqual(field.label.text, 'Čtečka paměťových karet:')

    def test_usb_c_charging_label(self):
        field = self.form._fields['usb_c_charging']
        self.assertEqual(field.label.text, 'USB-C nabíjení:')

    def test_battery_capacity_label(self):
        field = self.form._fields['battery_capacity']
        self.assertEqual(field.label.text, 'Kapacita baterie:')

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

    def test_usb_ports_label(self):
        field = self.form._fields['usb_ports']
        self.assertEqual(field.label.text, 'Počet USB portů:')

    def test_hdmi_ports_label(self):
        field = self.form._fields['hdmi_ports']
        self.assertEqual(field.label.text, 'Počet HDMI portů:')

    def test_audio_jack_label(self):
        field = self.form._fields['audio_jack']
        self.assertEqual(field.label.text, 'Audio Jack:')

    def test_usb_3_0_label(self):
        field = self.form._fields['usb_3_0']
        self.assertEqual(field.label.text, 'USB 3.0:')

    def test_usb_2_0_label(self):
        field = self.form._fields['usb_2_0']
        self.assertEqual(field.label.text, 'USB 2.0:')

    def test_cd_dvd_drive_label(self):
        field = self.form._fields['cd_dvd_drive']
        self.assertEqual(field.label.text, 'CD/DVD mechanika:')

    def test_brand_id_label(self):
        field = self.form._fields['brand_id']
        self.assertEqual(field.label.text, 'Značka:')

    def test_category_id_label(self):
        field = self.form._fields['category_id']
        self.assertEqual(field.label.text, 'Kategorie:')

    def test_product_image_label(self):
        field = self.form._fields['product_image']
        self.assertEqual(field.label.text, 'Foto *:')

    def test_additional_images_label(self):
        field = self.form._fields['additional_images']
        self.assertEqual(field.label.text, 'Další fotky:')
