from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

# Create your tests here.


class BaseViewTest(APITestCase):
    client = APIClient()

    def setUp(self):
        self.song = 'a'