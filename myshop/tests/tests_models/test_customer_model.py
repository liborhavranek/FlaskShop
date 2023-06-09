""" Libor Havránek App Copyright (C)  20.4 2023 """

import unittest

from sqlalchemy.exc import IntegrityError
from flask_login import LoginManager
from myshop import create_app, db
from myshop.models.customer_model import Customer
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
        self.login_manager = LoginManager()
        self.login_manager.init_app(self.app)
        super().setUp()

    def create_customer(self):
        self.customer = Customer()
        self.customer.username = "test_user"
        self.customer.email = "test@example.com"
        self.customer.phone_code = "+1"
        self.customer.phone = "123456789"
        self.customer.password = "password"

        self.customer.faktura_first_name = "faktura_first_name"
        self.customer.faktura_last_name = "faktura_last_name"
        self.customer.faktura_city = "faktura_city"
        self.customer.faktura_street = "faktura_street"
        self.customer.faktura_zipcode = "58"

        self.customer.dodej_first_name = "dodej_first_name"
        self.customer.dodej_last_name = "dodej_last_name"
        self.customer.dodej_company = "dodej_company"
        self.customer.dodej_city = "dodej_city"
        self.customer.dodej_street = "dodej_street"
        self.customer.dodej_zipcode = "58"
        self.customer.dodej_info = "dodej_info"
        self.customer.dodej_phone_code = "+1"
        self.customer.dodej_phone = "987654321"

        self.customer.firma_ico = "88888888"
        self.customer.firma_dic = "9999999999"
        self.customer.firma_bank_acc = "1234567890"
        self.customer.firma_bank_number = "0800"
        self.customer.firma_spec_symbol = "55555"
        db.session.add(self.customer)
        db.session.commit()

    def create_second_customer(self):
        self.second_customer = Customer()
        self.second_customer.username = "second_customer"
        self.second_customer.email = "test2@example.com"
        self.second_customer.phone = "123456789"
        self.second_customer.password = "password"

    def test_load_login_manager(self):
        customer = Customer()
        customer.username = "test_user"
        db.session.add(customer)
        db.session.commit()

        loaded_user = self.login_manager.user_loader(customer.id)

        self.assertEqual(loaded_user, customer.id)

    def test_load_user(self):
        self.create_customer()
        db.session.add(self.customer)
        db.session.commit()
        customer_id = self.customer.id

        loaded_user = Customer.query.get(customer_id)

        self.assertEqual(loaded_user, self.customer)

    def test_load_user_id(self, id=1):
        self.create_customer()
        db.session.add(self.customer)
        db.session.commit()

        loaded_user = Customer.query.get(id)

        self.assertEqual(loaded_user, self.customer)

    def test_load_user_with_valid_id(self):
        self.create_customer()
        db.session.add(self.customer)
        db.session.commit()
        customer_id = self.customer.id

        loaded_customer = self.login_manager.user_loader(customer_id)

        self.assertEqual(loaded_customer, customer_id)

    def test_customer_have_username(self):
        self.create_customer()
        result = Customer.query.filter_by(username="test_user").first()
        self.assertEqual(result.username, "test_user")

    def test_customer_have_email(self):
        self.create_customer()
        result = Customer.query.filter_by(username="test_user").first()
        self.assertEqual(result.email, "test@example.com")

    def test_customer_have_phone_code(self):
        self.create_customer()
        result = Customer.query.filter_by(username="test_user").first()
        self.assertEqual(result.phone_code, "+1")

    def test_customer_have_phone(self):
        self.create_customer()
        result = Customer.query.filter_by(username="test_user").first()
        self.assertEqual(result.phone, "123456789")

    def test_customer_have_password(self):
        self.create_customer()
        result = Customer.query.filter_by(username="test_user").first()
        self.assertEqual(result.password, "password")

    def test_customer_have_faktura_first_name(self):
        self.create_customer()
        result = Customer.query.filter_by(username="test_user").first()
        self.assertEqual(result.faktura_first_name, "faktura_first_name")

    def test_customer_have_faktura_last_name(self):
        self.create_customer()
        result = Customer.query.filter_by(username="test_user").first()
        self.assertEqual(result.faktura_last_name, "faktura_last_name")

    def test_customer_have_faktura_city(self):
        self.create_customer()
        result = Customer.query.filter_by(username="test_user").first()
        self.assertEqual(result.faktura_city, "faktura_city")

    def test_customer_have_faktura_street(self):
        self.create_customer()
        result = Customer.query.filter_by(username="test_user").first()
        self.assertEqual(result.faktura_street, "faktura_street")

    def test_customer_have_faktura_zipcode(self):
        self.create_customer()
        result = Customer.query.filter_by(username="test_user").first()
        self.assertEqual(result.faktura_zipcode, "58")

    def test_customer_have_dodej_first_name(self):
        self.create_customer()
        result = Customer.query.filter_by(username="test_user").first()
        self.assertEqual(result.dodej_first_name, "dodej_first_name")

    def test_customer_have_dodej_last_name(self):
        self.create_customer()
        result = Customer.query.filter_by(username="test_user").first()
        self.assertEqual(result.dodej_last_name, "dodej_last_name")

    def test_customer_have_dodej_company(self):
        self.create_customer()
        result = Customer.query.filter_by(username="test_user").first()
        self.assertEqual(result.dodej_company, "dodej_company")

    def test_customer_have_dodej_city(self):
        self.create_customer()
        result = Customer.query.filter_by(username="test_user").first()
        self.assertEqual(result.dodej_city, "dodej_city")

    def test_customer_have_dodej_street(self):
        self.create_customer()
        result = Customer.query.filter_by(username="test_user").first()
        self.assertEqual(result.dodej_street, "dodej_street")

    def test_customer_have_dodej_zipcode(self):
        self.create_customer()
        result = Customer.query.filter_by(username="test_user").first()
        self.assertEqual(result.dodej_zipcode, "58")

    def test_customer_have_dodej_info(self):
        self.create_customer()
        result = Customer.query.filter_by(username="test_user").first()
        self.assertEqual(result.dodej_info, "dodej_info")

    def test_customer_have_dodej_phone_code(self):
        self.create_customer()
        result = Customer.query.filter_by(username="test_user").first()
        self.assertEqual(result.dodej_phone_code, "+1")

    def test_customer_have_dodej_phone(self):
        self.create_customer()
        result = Customer.query.filter_by(username="test_user").first()
        self.assertEqual(result.dodej_phone, "987654321")

    def test_customer_have_firma_ico(self):
        self.create_customer()
        result = Customer.query.filter_by(username="test_user").first()
        self.assertEqual(result.firma_ico, "88888888")

    def test_second_user_have_id_two(self):
        self.create_customer()
        second_customer = Customer()
        second_customer.username = "second_customer"
        second_customer.email = "second_email@example.com"
        second_customer.phone_code = "+1"
        second_customer.phone = "987654321"
        second_customer.password = "password"
        db.session.add(second_customer)
        db.session.commit()
        result = Customer.query.filter_by(username="second_customer").first()
        self.assertEqual(result.id, 2)

    def test_in_db_cant_be_save_user_when_the_same_username(self):
        self.create_customer()

        # try to create a user with the same username
        with self.assertRaises(IntegrityError):
            second_customer = Customer()
            second_customer.username = "test_user"
            second_customer.email = "test2@example.com"
            second_customer.password = "password"
            db.session.add(second_customer)
            db.session.commit()

    def test_in_db_cant_be_save_user_when_the_same_email(self):
        self.create_customer()

        # try to create a user with the same username
        with self.assertRaises(IntegrityError):
            second_customer = Customer()
            second_customer.username = "test_user"
            second_customer.email = "test@example.com"
            second_customer.password = "password"
            db.session.add(second_customer)
            db.session.commit()

    def test_in_db_can_be_save_users_when_the_same_phonenumber(self):
        self.create_customer()
        second_customer = Customer()
        second_customer.username = "second_customer"
        second_customer.email = "test2@example.com"
        second_customer.phone = "123456789"
        second_customer.password = "password"
        db.session.add(second_customer)
        db.session.commit()
        customers = Customer.query.all()
        self.assertEqual(len(customers), 2)

    def test_in_db_can_be_save_users_when_the_same_password(self):
        self.create_customer()
        second_customer = Customer()
        second_customer.username = "second_customer"
        second_customer.email = "test2@example.com"
        second_customer.phone = "123456789"
        second_customer.password = "password"
        db.session.add(second_customer)
        db.session.commit()
        customers = Customer.query.all()
        self.assertEqual(len(customers), 2)

    def test_in_db_can_be_save_users_when_the_same_faktura_first_name(self):
        self.create_customer()
        self.create_second_customer()
        self.second_customer.faktura_first_name = "faktura_first_name"
        db.session.add(self.second_customer)
        db.session.commit()
        customers = Customer.query.all()
        self.assertEqual(len(customers), 2)

    def test_in_db_can_be_save_users_when_the_same_faktura_last_name(self):
        self.create_customer()
        self.create_second_customer()
        self.second_customer.faktura_last_name = "faktura_last_name"
        db.session.add(self.second_customer)
        db.session.commit()
        customers = Customer.query.all()
        self.assertEqual(len(customers), 2)

    def test_in_db_can_be_save_users_when_the_same_faktura_city(self):
        self.create_customer()
        self.create_second_customer()
        self.second_customer.faktura_city = "faktura_city"
        db.session.add(self.second_customer)
        db.session.commit()
        customers = Customer.query.all()
        self.assertEqual(len(customers), 2)

    def test_in_db_can_be_save_users_when_the_same_faktura_street(self):
        self.create_customer()
        self.create_second_customer()
        self.second_customer.faktura_street = "faktura_street"
        db.session.add(self.second_customer)
        db.session.commit()
        customers = Customer.query.all()
        self.assertEqual(len(customers), 2)

    def test_in_db_can_be_save_users_when_the_same_faktura_zipcode(self):
        self.create_customer()
        self.create_second_customer()
        self.second_customer.faktura_zipcode = "58"
        db.session.add(self.second_customer)
        db.session.commit()
        customers = Customer.query.all()
        self.assertEqual(len(customers), 2)

    def test_in_db_can_be_save_users_when_the_same_dodej_first_name(self):
        self.create_customer()
        self.create_second_customer()
        self.second_customer.dodej_first_name = "dodej_first_name"
        db.session.add(self.second_customer)
        db.session.commit()
        customers = Customer.query.all()
        self.assertEqual(len(customers), 2)

    def test_in_db_can_be_save_users_when_the_same_dodej_last_name(self):
        self.create_customer()
        self.create_second_customer()
        self.second_customer.dodej_last_name = "dodej_last_name"
        db.session.add(self.second_customer)
        db.session.commit()
        customers = Customer.query.all()
        self.assertEqual(len(customers), 2)

    def test_in_db_can_be_save_users_when_the_same_dodej_company(self):
        self.create_customer()
        self.create_second_customer()
        self.second_customer.dodej_company = "dodej_company"
        db.session.add(self.second_customer)
        db.session.commit()
        customers = Customer.query.all()
        self.assertEqual(len(customers), 2)

    def test_in_db_can_be_save_users_when_the_same_dodej_city(self):
        self.create_customer()
        self.create_second_customer()
        self.second_customer.dodej_city = "dodej_city"
        db.session.add(self.second_customer)
        db.session.commit()
        customers = Customer.query.all()
        self.assertEqual(len(customers), 2)

    def test_in_db_can_be_save_users_when_the_same_dodej_street(self):
        self.create_customer()
        self.create_second_customer()
        self.second_customer.dodej_street = "dodej_street"
        db.session.add(self.second_customer)
        db.session.commit()
        customers = Customer.query.all()
        self.assertEqual(len(customers), 2)

    def test_in_db_can_be_save_users_when_the_same_dodej_zipcode(self):
        self.create_customer()
        self.create_second_customer()
        self.second_customer.dodej_zipcode = "58"
        db.session.add(self.second_customer)
        db.session.commit()
        customers = Customer.query.all()
        self.assertEqual(len(customers), 2)

    def test_in_db_can_be_save_users_when_the_same_dodej_info(self):
        self.create_customer()
        self.create_second_customer()
        self.second_customer.dodej_info = "dodej_info"
        db.session.add(self.second_customer)
        db.session.commit()
        customers = Customer.query.all()
        self.assertEqual(len(customers), 2)

    def test_in_db_can_be_save_users_when_the_same_dodej_phone_code(self):
        self.create_customer()
        self.create_second_customer()
        self.second_customer.dodej_phone_code = "+1"
        db.session.add(self.second_customer)
        db.session.commit()
        customers = Customer.query.all()
        self.assertEqual(len(customers), 2)

    def test_in_db_can_be_save_users_when_the_same_dodej_phone(self):
        self.create_customer()
        self.create_second_customer()
        self.second_customer.dodej_phone = "987654321"
        db.session.add(self.second_customer)
        db.session.commit()
        customers = Customer.query.all()
        self.assertEqual(len(customers), 2)

    def test_in_db_can_be_save_users_when_the_same_firma_ico(self):
        self.create_customer()
        self.create_second_customer()
        self.second_customer.firma_ico = "88888888"
        db.session.add(self.second_customer)
        db.session.commit()
        customers = Customer.query.all()
        self.assertEqual(len(customers), 2)

    def test_in_db_can_be_save_users_when_the_same_firma_dic(self):
        self.create_customer()
        self.create_second_customer()
        self.second_customer.firma_dic = "9999999999"
        db.session.add(self.second_customer)
        db.session.commit()
        customers = Customer.query.all()
        self.assertEqual(len(customers), 2)

    def test_in_db_can_be_save_users_when_the_same_firma_bank_acc(self):
        self.create_customer()
        self.create_second_customer()
        self.second_customer.firma_bank_acc = "1234567890"
        db.session.add(self.second_customer)
        db.session.commit()
        customers = Customer.query.all()
        self.assertEqual(len(customers), 2)

    def test_in_db_can_be_save_users_when_the_same_firma_bank_number(self):
        self.create_customer()
        self.create_second_customer()
        self.second_customer.firma_bank_number = "0800"
        db.session.add(self.second_customer)
        db.session.commit()
        customers = Customer.query.all()
        self.assertEqual(len(customers), 2)

    def test_in_db_can_be_save_users_when_the_same_spec_symbol(self):
        self.create_customer()
        self.create_second_customer()
        self.second_customer.firma_spec_symbol = "55555"
        db.session.add(self.second_customer)
        db.session.commit()
        customers = Customer.query.all()
        self.assertEqual(len(customers), 2)

    # TODO after set passwords add tests to match password


class TestCustomerChangeModel(TestMixin, unittest.TestCase):
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

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def create_customer(self):
        self.customer = Customer()
        self.customer.username = "first_user"
        self.customer.email = "test@example.com"
        self.customer.phone_code = "+1"
        self.customer.phone = "123456789"
        self.customer.password = "password"

        self.customer.faktura_first_name = "faktura_first_name"
        self.customer.faktura_last_name = "faktura_last_name"
        self.customer.faktura_city = "faktura_city"
        self.customer.faktura_street = "faktura_street"
        self.customer.faktura_zipcode = "58"

        self.customer.dodej_first_name = "dodej_first_name"
        self.customer.dodej_last_name = "dodej_last_name"
        self.customer.dodej_company = "dodej_company"
        self.customer.dodej_city = "dodej_city"
        self.customer.dodej_street = "dodej_street"
        self.customer.dodej_zipcode = "58"
        self.customer.dodej_info = "dodej_info"
        self.customer.dodej_phone_code = "+1"
        self.customer.dodej_phone = "987654321"

        self.customer.firma_ico = "88888888"
        self.customer.firma_dic = "9999999999"
        self.customer.firma_bank_acc = "1234567890"
        self.customer.firma_bank_number = "0800"
        self.customer.firma_spec_symbol = "55555"
        db.session.add(self.customer)
        db.session.commit()

    def create_second_customers(self):
        self.second_user = Customer()
        self.second_user.username = "second_user"
        self.second_user.email = "test2@example.com"
        self.second_user.phone_code = "+1"
        self.second_user.phone = "987654321"
        self.customer.password = "password"
        db.session.add(self.second_user)
        db.session.commit()

    def test_update_username_when_username_is_not_used(self):
        self.create_customer()
        self.create_second_customers()
        self.second_user.username = "changed_username"
        db.session.commit()
        result = self.second_user.username
        self.assertEqual(result, "changed_username")

    def test_update_username_when_username_is_used(self):
        self.create_customer()
        self.create_second_customers()
        with self.assertRaises(IntegrityError):
            self.second_user.username = "first_user"
            db.session.commit()

    def test_update_username_when_email_is_not_used(self):
        self.create_customer()
        self.create_second_customers()
        self.second_user.email = "changed@email.com"
        db.session.commit()
        result = self.second_user.email
        self.assertEqual(result, "changed@email.com")

    def test_update_username_when_email_is_used(self):
        self.create_customer()
        self.create_second_customers()
        with self.assertRaises(IntegrityError):
            self.second_user.email = "test@example.com"
            db.session.commit()

    def test_update_username_when_phone_is_not_used(self):
        self.create_customer()
        self.create_second_customers()
        self.second_user.phone = "111999111"
        db.session.commit()
        result = self.second_user.phone
        self.assertEqual(result, "111999111")

    def test_update_username_when_phone_used(self):
        self.create_customer()
        self.create_second_customers()
        self.second_user.phone = "123456789"
        db.session.commit()
        result = self.second_user.phone
        self.assertEqual(result, "123456789")

    def test_factura_first_name_can_be_changed(self):
        self.create_customer()
        self.customer.faktura_first_name = "faktura_first_name_changed"
        db.session.commit()
        result = self.customer.faktura_first_name
        self.assertEqual(result, "faktura_first_name_changed")

    def test_factura_last_name_can_be_changed(self):
        self.create_customer()
        self.customer.faktura_last_name = "faktura_last_name_changed"
        db.session.commit()
        result = self.customer.faktura_last_name
        self.assertEqual(result, "faktura_last_name_changed")

    def test_factura_city_can_be_changed(self):
        self.create_customer()
        self.customer.faktura_city = "faktura_city_changed"
        db.session.commit()
        result = self.customer.faktura_city
        self.assertEqual(result, "faktura_city_changed")

    def test_factura_street_can_be_changed(self):
        self.create_customer()
        self.customer.faktura_street = "faktura_street_changed"
        db.session.commit()
        result = self.customer.faktura_street
        self.assertEqual(result, "faktura_street_changed")

    def test_factura_zipcode_can_be_changed(self):
        self.create_customer()
        self.customer.faktura_zipcode = "333"
        db.session.commit()
        result = self.customer.faktura_zipcode
        self.assertEqual(result, "333")

    def test_dodej_first_name_can_be_changed(self):
        self.create_customer()
        self.customer.dodej_first_name = "dodej_first_name_changed"
        db.session.commit()
        result = self.customer.dodej_first_name
        self.assertEqual(result, "dodej_first_name_changed")

    def test_dodej_last_name_can_be_changed(self):
        self.create_customer()
        self.customer.dodej_last_name = "dodej_last_name_changed"
        db.session.commit()
        result = self.customer.dodej_last_name
        self.assertEqual(result, "dodej_last_name_changed")

    def test_dodej_company_can_be_changed(self):
        self.create_customer()
        self.customer.dodej_company = "dodej_company_changed"
        db.session.commit()
        result = self.customer.dodej_company
        self.assertEqual(result, "dodej_company_changed")

    def test_dodej_city_can_be_changed(self):
        self.create_customer()
        self.customer.dodej_city = "dodej_city_changed"
        db.session.commit()
        result = self.customer.dodej_city
        self.assertEqual(result, "dodej_city_changed")

    def test_dodej_street_can_be_changed(self):
        self.create_customer()
        self.customer.dodej_street = "dodej_street_changed"
        db.session.commit()
        result = self.customer.dodej_street
        self.assertEqual(result, "dodej_street_changed")

    def test_dodej_zipcode_can_be_changed(self):
        self.create_customer()
        self.customer.dodej_zipcode = "444"
        db.session.commit()
        result = self.customer.dodej_zipcode
        self.assertEqual(result, "444")

    def test_dodej_info_can_be_changed(self):
        self.create_customer()
        self.customer.dodej_info = "dodej_info_changed"
        db.session.commit()
        result = self.customer.dodej_info
        self.assertEqual(result, "dodej_info_changed")

    def test_dodej_phone_code_can_be_changed(self):
        self.create_customer()
        self.customer.dodej_phone_code = "420"
        db.session.commit()
        result = self.customer.dodej_phone_code
        self.assertEqual(result, "420")

    def test_dodej_phone_can_be_changed(self):
        self.create_customer()
        self.customer.dodej_phone = "123456789"
        db.session.commit()
        result = self.customer.dodej_phone
        self.assertEqual(result, "123456789")

    def test_firma_ico_can_be_changed(self):
        self.create_customer()
        self.customer.firma_ico = "66666666"
        db.session.commit()
        result = self.customer.firma_ico
        self.assertEqual(result, "66666666")

    def test_firma_dic_can_be_changed(self):
        self.create_customer()
        self.customer.firma_dic = "1111111111"
        db.session.commit()
        result = self.customer.firma_dic
        self.assertEqual(result, "1111111111")

    def test_firma_bank_acc_can_be_changed(self):
        self.create_customer()
        self.customer.firma_bank_acc = "0987654321"
        db.session.commit()
        result = self.customer.firma_bank_acc
        self.assertEqual(result, "0987654321")

    def test_firma_bank_number_can_be_changed(self):
        self.create_customer()
        self.customer.firma_bank_number = "5000"
        db.session.commit()
        result = self.customer.firma_bank_number
        self.assertEqual(result, "5000")

    def test_firma_spec_symbol_can_be_changed(self):
        self.create_customer()
        self.customer.firma_spec_symbol = "77777"
        db.session.commit()
        result = self.customer.firma_spec_symbol
        self.assertEqual(result, "77777")

    # TODO IF if it will possible add tests for change password

    def test_delete_customer(self):
        self.create_customer()
        db.session.delete(self.customer)
        db.session.commit()
        result = Customer.query.filter_by(username="test_user").first()
        self.assertIsNone(result)
