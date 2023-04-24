""" Libor Havránek App Copyright (C)  21.4 2023 """

from myshop.tests.my_test_mixin import TestAllTemplates


class TestEditBrand(TestAllTemplates):
    """Test edit brand page."""

    path = '/products/create-product'

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
