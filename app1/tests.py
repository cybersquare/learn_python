from django.test import TestCase
from django.urls import reverse, resolve
from .views import first
# from django.test import SimpleTestCase
# Create your tests here.

from rest_framework.test import APIClient
from rest_framework import status

# command: python manage.py test app1

class TestSample(TestCase):

    def setup(self):
        self.client = APIClient

    def test_sample(self): #Method name shoudl start with 'test'
        print('hello')
        url = reverse('first_api')
        # print(resolve(url))
        res = self.client.get(url)
        print(res.data)
        self.assertEquals(res.status_code, 200 )
        self.assertEquals(res.data, 'Congratulations, you  have created an API' )
        # assert 1==2

# 'Congratulations, you  have created an API '