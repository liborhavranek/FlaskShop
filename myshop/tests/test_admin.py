""" Libor Havránek App Copyright (C)  23.3 2023 """

import unittest

from myshop import create_app


class TestCreateApp(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.testing = True

    def test_view_have_set_correct_template(self):
        with self.app.test_client() as client:
            response = client.get('/admin')
            self.assertTrue(response, 'admin.html')


if __name__ == '__main__':
    unittest.main()
