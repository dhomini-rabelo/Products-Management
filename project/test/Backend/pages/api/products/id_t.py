import json
from django.test import Client
from backend.Api.serializers.products import ProductSerializer
from backend.products.app.models import Product
from .. import TestModelDataListApi
from random import randint


class TestProductDetailApi(TestModelDataListApi):

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.create_models(cls)
        cls.create_user(cls)
        cls.request = cls.client.get('/api/products/1')

    def test_status_without_login(self):
        self.assertEqual(self.request.status_code, 403)

    def test_status_with_login(self):
        self.login()
        self.request = self.client.get('/api/products/1')
        self.assertEqual(self.request.status_code, 200)

    def test_data(self):
        self.login()
        self.request = self.client.get('/api/products/1')
        serializer = ProductSerializer(Product.objects.get(id=1))
        self.assertEqual(
            self.request.data,
            serializer.data
        )

    def test_put_method(self):
        self.login()
        new_data = {
            'name' : 'Test put method',
            'price' : '150000000.50',
            'quantity' : randint(1, 500),
            'category' : self.categories[randint(0, 2)].id,
        }
        self.request = self.client.put('/api/products/1', data=json.dumps(new_data), content_type='application/json')
        request_data = self.request.data.copy()
        for remove_ in ['id', 'created', 'updated', 'category']: del request_data[remove_]
        del new_data['category']
        self.assertEqual(request_data, new_data)

    def test_delete_method(self):
        self.login()
        self.request = self.client.delete('/api/products/1')
        self.assertEqual(self.request.status_code, 204)
