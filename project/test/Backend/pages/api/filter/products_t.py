from concurrent.futures import process
from django.test import TestCase, Client
from backend.Api.serializers.products import ProductSerializer
from backend.accounts.app.models import User
from backend.products.app.models import Product
from backend.categories.app.models import Category
from rest_framework.pagination import PageNumberPagination
from decimal import Decimal
from random import randint
from pprint import pprint
from .. import TestModelDataListApi
from backend.Api.actions.objects.products import product_filters




class TestProductListApi(TestModelDataListApi):

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.create_models(cls)
        cls.create_user(cls)
        cls.request = cls.client.get('/api/products/filter')

    def test_status(self):
        self.assertEqual(self.request.status_code, 200) 

    def test_data(self):
        serializer = ProductSerializer(Product.objects.order_by('id'), many=True)
        self.assertEqual(
            self.request.data,
            serializer.data
        )

    def test_filters_individually(self):
        for query_name, query in product_filters.items():
            values = {
                'name': 'product',
                'price': '500.50',
                'quantity': '50',
                'category': 'category 3',
            }
            value = values[query_name]
            request = self.client.get(f'/api/products/filter?{query_name}={value}')
            serializer = ProductSerializer(Product.objects.filter(**{query: value}).order_by('id'), many=True)
            self.assertEqual(
                request.data,
                serializer.data
            )

    def test_filters_in_group(self):
        for query_name, query in product_filters.items():
            values = {
                'name': 'product',
                'price': '500.50',
                'quantity': '50',
                'category': 'category 3',
            }
            value = values[query_name]
            others_query = list(product_filters.keys()).copy()
            others_query.pop(others_query.index(query_name))
            for other_query in others_query:
                other_query_value = values[other_query]
                url = f'/api/products/filter?{query_name}={value}&{other_query}={other_query_value}'
                request = self.client.get(url)
                filter_query = {query: value, product_filters[other_query]: other_query_value}
                serializer = ProductSerializer(Product.objects.filter(**filter_query).order_by('id'), many=True)
                self.assertEqual(
                    request.data,
                    serializer.data
                )
            
    
    def test_filters_with_invalid_query_name(self):
        query_name = 'invalid'
        request = self.client.get(f'/api/products/filter?{query_name}=none')
        self.assertEqual(
            request.status_code,
            400
        )
        self.assertEqual(
            request.data,
            {
                'error': 'KeyError',
                'invalid_key': query_name
            } 
        )







