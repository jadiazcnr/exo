from django.test import TestCase
from rates.provider import RateDataProvider


class RatesTestCase(TestCase):

    def setUp(self):
        self.provider = RateDataProvider("Mock")

    def test_invalid_provider(self):
        self.assertRaises(ValueError, RateDataProvider, "test")

    def test_get_rates_between_dates(self):
        result = self.provider.get_rates_between_dates("2018-01-01", "2018-01-01")
        self.assertTrue(result.get("success"), True)

    def test_convert(self):
        result = self.provider.convert("EUR", "GPR", 10)
        self.assertTrue(result.get("success"), True)

    def test_calculate_fluctuaction(self):
        result = self.provider.calculate_fluctuaction("EUR", "GPR", "2018-01-01", "2018-02-01")
        self.assertTrue(result.get("success"), True)

    def test_calculate_fluctuaction_change(self):
        result = self.provider.calculate_fluctuaction("EUR", "USD", "2018-01-01", "2018-02-01")
        self.assertTrue(result.get("rates").get("USD").get("change"), True)
