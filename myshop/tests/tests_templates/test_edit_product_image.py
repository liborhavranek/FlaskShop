""" Libor Havránek App Copyright (C)  7.5 2023 """


from myshop.tests.my_test_mixin import TestAllTemplates


class TestProductList(TestAllTemplates):
    """Test edit brand page."""

    path = '/products/edit-product-images/1'

    @classmethod
    def setUpClass(cls):
        super().setUpClass()