from django.test import Client
from backend.Api.serializers.categories import CategorySerializer
from backend.accounts.app.models import User
from backend.categories.app.models import Category
from backend.Api.serializers.products import ProductSerializer
from backend.products.app.models import Product
from .. import TestModelDataListApi
from random import randint
import json




class TestCategoryDetailApi(TestModelDataListApi):

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.create_models(cls)
        cls.create_user(cls)
        cls.request = cls.client.get('/api/categories/1')

    def test_status_without_login(self):
        self.assertEqual(self.request.status_code, 403)

    def test_status_with_login(self):
        self.login()
        self.request = self.client.get('/api/categories/1')
        self.assertEqual(self.request.status_code, 200)

    def test_data(self):
        self.login()
        self.request = self.client.get('/api/categories/1')
        serializer = CategorySerializer(Category.objects.get(id=1))
        self.assertEqual(
            self.request.data,
            serializer.data
        )

    def test_put_method(self):
        self.login()
        new_data = {
            'name' : 'Test put method',
        }
        self.request = self.client.put('/api/categories/1', data=json.dumps(new_data), content_type='application/json')
        self.assertEqual(self.request.data, {**new_data, 'id': 1})

    def test_delete_method(self):
        self.login()
        self.request = self.client.delete('/api/categories/1')
        self.assertEqual(self.request.status_code, 204)
