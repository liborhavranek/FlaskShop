""" Libor Havránek App Copyright (C)  23.3 2023 """

import unittest

from flask_login import current_user, logout_user
from werkzeug.security import generate_password_hash
from myshop.tests.my_test_mixin import TestMixin

from myshop import create_app, db
from myshop.models import Customer


class TestAuthRegister(TestMixin, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_name = cls.__name__

    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()
        app_context = self.app.app_context()
        app_context.push()
        db.create_all()
        super().setUp()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    @staticmethod
    def create_user():
        new_customer = Customer()

        new_customer.username = 'john_doe'
        new_customer.email = 'john.doe@example.com'
        new_customer.phone_code = '1'
        new_customer.phone = '1234567890'
        new_customer.password = generate_password_hash('mypassword', method='sha256')
        new_customer.faktura_first_name = 'John'
        new_customer.faktura_last_name = 'Doe'
        new_customer.faktura_city = 'New York'
        new_customer.faktura_street = '123 Main St'
        new_customer.faktura_zipcode = '10001'
        new_customer.dodej_first_name = 'John'
        new_customer.dodej_last_name = 'Doe'
        new_customer.dodej_company = 'ACME Inc.'
        new_customer.dodej_city = 'New York'
        new_customer.dodej_street = '123 Main St'
        new_customer.dodej_zipcode = '10001'
        new_customer.dodej_info = 'Delivery instructions'
        new_customer.dodej_phone_code = '1'
        new_customer.dodej_phone = '1234567890'
        new_customer.firma_ico = '123456789'
        new_customer.firma_dic = '987654321'
        new_customer.firma_bank_acc = '0123456789'
        new_customer.firma_bank_number = '0800'
        new_customer.firma_spec_symbol = '1234'

        db.session.add(new_customer)
        db.session.commit()

    def test_view_have_set_correct_template(self):
        response = self.client.get('/auth')
        self.assertTrue(response, 'auth.html')

    def test_auth_route_returns_correct_status_code(self):
        response = self.client.get('/auth', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_auth_register_return_correct_status_code_when_match_passwords(self):
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "phone_code": "+1",
            "phone": "1234567890",
            "password": "password",
            "confirm_password": "password"
        }
        response = self.client.post('/auth/register', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_auth_register_return_template_when_match_passwords(self):
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "phone_code": "+1",
            "phone": "1234567890",
            "password": "password",
            "confirm_password": "password"
        }
        response = self.client.post('/auth/register', data=data, follow_redirects=True)
        self.assertTrue(response, 'index.html')

    def test_auth_register_return_correct_correct_status_code_when_mismatch_passwords(self):
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "phone_code": "+1",
            "phone": "1234567890",
            "password": "password",
            "confirm_password": "password2"
        }
        response = self.client.post('/auth/register', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_register_with_mismatched_passwords_return_correct_message(self):
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "phone_code": "+1",
            "phone": "1234567890",
            "password": "password",
            "confirm_password": "password2"
        }
        response = self.client.post('/auth/register', data=data, follow_redirects=True)
        self.assertIn(bytes("Heslo a potvrzení hesla se musí shodovat.", "utf-8"), response.data)

    def test_auth_register_return_correct_template_when_missmatch_passwords(self):
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "phone_code": "+1",
            "phone": "1234567890",
            "password": "password",
            "confirm_password": "password2"
        }
        response = self.client.post('/auth/register', data=data, follow_redirects=True)
        self.assertTrue(response, 'login.html')

    def test_username_is_save_username_in_database_when_create_account(self):
        self.create_user()
        new_customer = Customer.query.filter_by(email='john.doe@example.com').first()
        self.assertEqual(new_customer.username, 'john_doe')

    def test_username_is_save_email_in_database_when_create_account(self):
        self.create_user()
        new_customer = Customer.query.filter_by(email='john.doe@example.com').first()
        self.assertEqual(new_customer.email, 'john.doe@example.com')

    def test_username_is_save_phone_code_in_database_when_create_account(self):
        self.create_user()
        new_customer = Customer.query.filter_by(email='john.doe@example.com').first()
        self.assertEqual(new_customer.phone_code, '1')

    def test_username_is_save_phone_in_database_when_create_account(self):
        self.create_user()
        new_customer = Customer.query.filter_by(email='john.doe@example.com').first()
        self.assertEqual(new_customer.phone, '1234567890')

    def test_username_is_save_faktura_first_name_in_database_when_create_account(self):
        self.create_user()
        new_customer = Customer.query.filter_by(email='john.doe@example.com').first()
        self.assertEqual(new_customer.faktura_first_name, 'John')

    def test_username_is_save_faktura_last_name_in_database_when_create_account(self):
        self.create_user()
        new_customer = Customer.query.filter_by(email='john.doe@example.com').first()
        self.assertEqual(new_customer.faktura_last_name, 'Doe')

    def test_username_is_save_faktura_city_in_database_when_create_account(self):
        self.create_user()
        new_customer = Customer.query.filter_by(email='john.doe@example.com').first()
        self.assertEqual(new_customer.faktura_city, 'New York')

    def test_username_is_save_faktura_street_in_database_when_create_account(self):
        self.create_user()
        new_customer = Customer.query.filter_by(email='john.doe@example.com').first()
        self.assertEqual(new_customer.faktura_street, '123 Main St')

    def test_username_is_save_faktura_zipcode_in_database_when_create_account(self):
        self.create_user()
        new_customer = Customer.query.filter_by(email='john.doe@example.com').first()
        self.assertEqual(new_customer.faktura_zipcode, '10001')

    def test_username_is_save_dodej_first_name_in_database_when_create_account(self):
        self.create_user()
        new_customer = Customer.query.filter_by(email='john.doe@example.com').first()
        self.assertEqual(new_customer.dodej_first_name, 'John')

    def test_username_is_save_dodej_last_name_in_database_when_create_account(self):
        self.create_user()
        new_customer = Customer.query.filter_by(email='john.doe@example.com').first()
        self.assertEqual(new_customer.dodej_last_name, 'Doe')

    def test_username_is_save_dodej_company_in_database_when_create_account(self):
        self.create_user()
        new_customer = Customer.query.filter_by(email='john.doe@example.com').first()
        self.assertEqual(new_customer.dodej_company, 'ACME Inc.')

    def test_username_is_save_dodej_city_in_database_when_create_account(self):
        self.create_user()
        new_customer = Customer.query.filter_by(email='john.doe@example.com').first()
        self.assertEqual(new_customer.dodej_city, 'New York')

    def test_username_is_save_dodejstreet_in_database_when_create_account(self):
        self.create_user()
        new_customer = Customer.query.filter_by(email='john.doe@example.com').first()
        self.assertEqual(new_customer.dodej_street, '123 Main St')

    def test_username_is_save_dodej_zipcode_in_database_when_create_account(self):
        self.create_user()
        new_customer = Customer.query.filter_by(email='john.doe@example.com').first()
        self.assertEqual(new_customer.dodej_zipcode, '10001')

    def test_username_is_save_dodej_info_in_database_when_create_account(self):
        self.create_user()
        new_customer = Customer.query.filter_by(email='john.doe@example.com').first()
        self.assertEqual(new_customer.dodej_info, 'Delivery instructions')

    def test_username_is_save_dodej_phone_code_in_database_when_create_account(self):
        self.create_user()
        new_customer = Customer.query.filter_by(email='john.doe@example.com').first()
        self.assertEqual(new_customer.dodej_phone_code, '1')

    def test_username_is_save_dodej_phone_in_database_when_create_account(self):
        self.create_user()
        new_customer = Customer.query.filter_by(email='john.doe@example.com').first()
        self.assertEqual(new_customer.dodej_phone, '1234567890')

    def test_username_is_save_firma_ico_in_database_when_create_account(self):
        self.create_user()
        new_customer = Customer.query.filter_by(email='john.doe@example.com').first()
        self.assertEqual(new_customer.firma_ico, '123456789')

    def test_username_is_save_firma_dic_in_database_when_create_account(self):
        self.create_user()
        new_customer = Customer.query.filter_by(email='john.doe@example.com').first()
        self.assertEqual(new_customer.firma_dic, '987654321')

    def test_username_is_save_firma_bank_acc_in_database_when_create_account(self):
        self.create_user()
        new_customer = Customer.query.filter_by(email='john.doe@example.com').first()
        self.assertEqual(new_customer.firma_bank_acc, '0123456789')

    def test_username_is_save_firma_bank_number_in_database_when_create_account(self):
        self.create_user()
        new_customer = Customer.query.filter_by(email='john.doe@example.com').first()
        self.assertEqual(new_customer.firma_bank_number, '0800')

    def test_username_is_save_firma_spec_szmbol_in_database_when_create_account(self):
        self.create_user()
        new_customer = Customer.query.filter_by(email='john.doe@example.com').first()
        self.assertEqual(new_customer.firma_spec_symbol, '1234')


if __name__ == '__main__':
    unittest.main()


class TestAuth(TestMixin, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_name = cls.__name__

    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()
        app_context = self.app.app_context()
        app_context.push()
        db.create_all()
        super().setUp()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_login_with_valid_credentials_return_correct_status_code(self):
        user_password = "password"
        customer = Customer()
        customer.username = "testuser"
        customer.email = "testuser@example.com"
        customer.user_password = generate_password_hash(user_password, method='sha256')
        db.session.add(customer)
        db.session.commit()
        data = {
            "email": "testuser@example.com",
            "password": "password"
        }
        response = self.client.post('/auth/login', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_login_with_valid_credentials_return_correct_template(self):
        user_password = "password"
        customer = Customer()
        customer.username = "testuser"
        customer.email = "testuser@example.com"
        customer.user_password = generate_password_hash(user_password, method='sha256')
        db.session.add(customer)
        db.session.commit()
        data = {
            "email": "testuser@example.com",
            "password": "password"
        }
        response = self.client.post('/auth/login', data=data, follow_redirects=True)
        self.assertTrue(response, 'index.html')

    def test_login_with_valid_credentials_return_correct_message(self):
        user_password = "password"
        customer = Customer()
        customer.username = "testuser"
        customer.email = "testuser@example.com"
        customer.user_password = generate_password_hash(user_password, method='sha256')
        db.session.add(customer)
        db.session.commit()
        data = {
            "email": "testuser@example.com",
            "password": "password"
        }
        response = self.client.post('/auth/login', data=data, follow_redirects=True)
        self.assertIn(bytes("Úspěšně jsi se přihlásil.", "utf-8"), response.data)

    def test_login_with_invalid_credentials_return_correct_status_code(self):
        user_password = "password"
        customer = Customer()
        customer.username = "testuser"
        customer.email = "testuser@example.com"
        customer.user_password = generate_password_hash(user_password, method='sha256')
        db.session.add(customer)
        db.session.commit()
        data = {
            "email": "testuser@example.com",
            "password": "wrongpassword"
        }
        response = self.client.post('/auth/login', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_login_with_invalid_credentials_return_correct_template(self):
        password = "password"
        customer = Customer()
        customer.username = "testuser"
        customer.email = "testuser@example.com"
        customer.user_password = generate_password_hash(password, method='sha256')
        db.session.add(customer)
        db.session.commit()
        data = {
            "email": "testuser@example.com",
            "password": "wrongpassword"
        }
        response = self.client.post('/auth/login', data=data, follow_redirects=True)
        self.assertTrue(response, 'login.html')

    def test_login_with_invalid_password_return_correct_message(self):
        user_password = "password"
        customer = Customer()
        customer.username = "testuser"
        customer.email = "testuser@example.com"
        customer.user_password = generate_password_hash(user_password, method='sha256')
        db.session.add(customer)
        db.session.commit()
        data = {
            "email": "testuser@example.com",
            "password": "wrongpassword"
        }
        response = self.client.post('/auth/login', data=data, follow_redirects=True)
        self.assertIn(bytes("Zadal jsi nesprávné heslo.", "utf-8"), response.data)

    def test_login_with_invalid_email_return_correct_message(self):
        password = "password"
        customer = Customer()
        customer.username = "testuser"
        customer.email = "testuser@example.com"
        customer.password = generate_password_hash(password, method='sha256')
        db.session.add(customer)
        db.session.commit()
        data = {
            "email": "wrongemail@example.com",
            "password": "password"
        }
        response = self.client.post('/auth/login', data=data, follow_redirects=True)
        self.assertIn(bytes("Email neexistuje.", "utf-8"), response.data)

    def test_logout_return_correct_status_code(self):
        self.client.post('/auth/login', data={"email": "testuser@example.com", "password": "password"})
        response = self.client.get('/auth/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_logout_return_correct_template(self):
        self.client.post('/auth/login', data={"email": "testuser@example.com", "password": "password"})
        response = self.client.get('/auth/logout', follow_redirects=True)
        self.assertTrue(response, 'index.html')

    def test_logout_user(self):
        with self.app.test_request_context('/logout'):
            logout_user()
            self.assertTrue(current_user.is_anonymous)

    def test_create_test_data(self):
        """this I will change all time"""
        response = self.client.get('/auth/create-customers', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        customers = Customer.query.all()
        self.assertEqual(len(customers), 2)


if __name__ == '__main__':
    unittest.main()
