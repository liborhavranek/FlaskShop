""" Libor Havránek App Copyright (C)  9.6 2023 """

from myshop.tests.my_test_mixin import TestAllTemplates


class TestCartTemplate(TestAllTemplates):
    """Test auth page."""

    path = "/cart"

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
