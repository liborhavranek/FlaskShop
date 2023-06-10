""" Libor Havránek App Copyright (C)  18.4 2023 """

from myshop.tests.my_test_mixin import TestAllTemplates


class TestEditBrand(TestAllTemplates):
    """Test edit brand page."""

    path = "/products/create-category"

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
