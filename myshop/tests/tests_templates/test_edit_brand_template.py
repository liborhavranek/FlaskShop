""" Libor Havránek App Copyright (C)  17.4 2023 """

from myshop.tests.my_test_mixin import TestAllTemplates


class TestEditBrand(TestAllTemplates):
    """Test edit brand page."""

    path = '/products/edit-brand/1'

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
