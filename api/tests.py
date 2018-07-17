from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse


class ModelTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.rates_data = {'date-from': '2017-01-01', 'date-to': '2018-01-01'}
        self.convert_data = {'origin': 'EUR', 'target': 'USD', 'amount': 10}
        self.time_weighted_rate = {'origin': 'EUR', 'target': 'USD', 'amount': 10, 'date-invested': '2017-01-01'}

    def test_get_rates_ok(self):
        response = self.client.get(reverse('rates'), self.rates_data, format="json")
        self.assertEqual(response.status_code, 200)

    def test_get_rates(self):
        response = self.client.get(reverse('rates'), self.rates_data, format="json").json()
        self.assertTrue(response.get("success"), True)

    def test_get_rates_bad_params(self):
        rates_data = {'date-from': '2017-01-01'}
        response = self.client.get(reverse('rates'), rates_data, format="json").json()
        self.assertDictEqual(response, {"2": "date-to is required"})

    def test_convert_ok(self):
        response = self.client.get(reverse('convert'), self.convert_data, format="json")
        self.assertEqual(response.status_code, 200)

    def test_convert(self):
        response = self.client.get(reverse('convert'), self.convert_data, format="json").json()
        self.assertTrue(response.get("success"), True)

    def test_convert_bad_params(self):
        convert_data = {'origin': 'ASD', 'target': 'USD', 'amount' : 10}
        response = self.client.get(reverse('convert'), convert_data, format="json").json()
        self.assertDictEqual(response, {'6': 'origin has to be one of EUR CHF USD GBP'})

    def test_time_weighted_rate_ok(self):
        response = self.client.get(reverse('time_weighted_rate'), self.time_weighted_rate, format="json")
        self.assertEqual(response.status_code, 200)

    def test_time_weighted_rate(self):
        response = self.client.get(reverse('time_weighted_rate'), self.time_weighted_rate, format="json").json()
        self.assertTrue(response.get("success"), True)

    def test_time_weighted_rate_bad_params(self):
        time_weighted_rate = {'origin': 'ASD', 'target': 'USD', 'amount' : 10}
        response = self.client.get(reverse('time_weighted_rate'), time_weighted_rate, format="json").json()
        self.assertDictEqual(response, {'2': 'date-invested is required',
                                        '6': 'origin has to be one of EUR CHF USD GBP'})
