""" Libor Havránek App Copyright (C)  13.4 2023 """


from myshop.tests.my_test_mixin import TestAllTemplates


class TestProductList(TestAllTemplates):
    """Test edit brand page."""

    path = '/products/products-list'

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
