""" Libor Havránek App Copyright (C)  23.3 2023 """

import unittest

from myshop import create_app
from myshop.tests.my_test_mixin import TestMixin, TestAllTemplates


class TestAuthTemplate(TestAllTemplates):
    """Test auth page."""

    path = '/auth'

    @classmethod
    def setUpClass(cls):
        super().setUpClass()


class TestAuthTemplateOnlyAuthTemplate(TestMixin, unittest.TestCase):
    """Test what are specific only for this template"""

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

    def test_response_status(self):
        response = self.client.get('/auth', follow_redirects=True)
        self.assertIn(b'auth web', response.data)


if __name__ == '__main__':
    unittest.main()
