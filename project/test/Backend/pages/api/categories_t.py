from concurrent.futures import process
from django.test import TestCase, Client
from backend.Api.serializers.categories import CategorySerializer
from backend.accounts.app.models import User
from backend.products.app.models import Product
from backend.categories.app.models import Category
from rest_framework.pagination import PageNumberPagination
from decimal import Decimal
from random import randint
from pprint import pprint
from . import TestModelDataListApi




class TestCategoryListApi(TestModelDataListApi):

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.create_models(cls)
        cls.create_user(cls)
        cls.request = cls.client.get('/api/categories')

    def test_status(self):
        self.assertEqual(self.request.status_code, 200) 

    def test_data(self):
        serializer = CategorySerializer(Category.objects.order_by('id'), many=True)
        self.assertEqual(
            self.request.data['results'],
            serializer.data
        )

    def test_create_category_without_login(self):
        post_request = self.client.post('/api/categories', data = {
            'name' : 'Test Category',
        })
        self.assertEqual(post_request.status_code, 403)

    def test_create_category_with_login(self):
        self.client.login(username='test', password='testing')
        post_request = self.client.post('/api/categories', data = {
            'name' : 'Test PCategory',
        }, follow=True)
        self.assertEqual(post_request.status_code, 200)
