""" Libor Havránek App Copyright (C)  23.3 2023 """

import unittest

from myshop import create_app
from myshop.tests.my_test_mixin import TestMixin


class TestCreateApp(TestMixin, unittest.TestCase):

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

    def test_view_have_set_correct_template(self):
        with self.app.test_client() as client:
            response = client.get('/admin')
            self.assertTrue(response, 'admin.html')


if __name__ == '__main__':
    unittest.main()
