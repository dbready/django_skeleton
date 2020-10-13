from django.test import TestCase

from core.forms import CalcForm


class CoreFormsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        pass

    def test_calc(self):
        """Example testing of the CalcForm"""
        left = 1
        right = 2
        form_data = {"num_one": left, "num_two": right}
        form = CalcForm(form_data)
        self.assertTrue(form.is_valid())
        if form.is_valid():
            self.assertEqual(left + right, 3)
