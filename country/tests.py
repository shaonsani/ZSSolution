import json
from django.urls import reverse
from country.models import Country
from country.serializers import CountrySerializer
from django.test import TestCase, Client
from rest_framework import status

client = Client()

class CountryListTestCase(TestCase):
    country_list_url = reverse("country_list")

    def setUp(self):
        Country.objects.create(name='India', latitude=37.45, longitude=14.45, code='IND')
        Country.objects.create(name='Bhutan', latitude=37.45, longitude=14.45, code='BHT')

    def test_country_list(self):
        # get API response
        response = client.get(f'{self.country_list_url}?page=1&limit=10')
        # get data from db
        country_list = Country.objects.all()
        serializer = CountrySerializer(country_list, many=True)
        self.assertEqual(response.data['data'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_country_list_with_filter(self):
        # get API response
        response = client.get(f'{self.country_list_url}?page=1&limit=10&name=India')
        # get data from db
        country_list = Country.objects.filter(name='India')
        serializer = CountrySerializer(country_list, many=True)
        self.assertEqual(response.data['data'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_country_list_with_blank_filter(self):
        # get API response
        response = client.get(f'{self.country_list_url}?page=1&limit=10&name=')
        # get data from db
        country_list = Country.objects.all()
        serializer = CountrySerializer(country_list, many=True)
        self.assertEqual(response.data['data'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_country_list_error_response(self):
        # get API response
        response = client.get(f'{self.country_list_url}')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)