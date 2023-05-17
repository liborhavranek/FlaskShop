""" Libor Havránek App Copyright (C)  17.5. 2023 """

from myshop.tests.my_test_mixin import TestAllTemplates


class TestEditBrand(TestAllTemplates):
    """Test edit brand page."""

    path = '/products/create-notebook-product'

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
