""" Libor Havránek App Copyright (C)  23.3 2023 """

import unittest

from myshop import create_app
from myshop.tests.my_test_mixin import TestMixin


class TestCreateApp(TestMixin, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_name = cls.__name__

    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        super().setUp()

    def test_view_have_set_correct_template(self):
        with self.app.test_client() as client:
            response = client.get('/')
            self.assertTrue(response, 'views.html')


if __name__ == '__main__':
    unittest.main()
