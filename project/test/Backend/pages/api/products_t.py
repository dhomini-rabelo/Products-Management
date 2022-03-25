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


class TestCategoryListApi(TestCase):


    def create_models(self):      
        self.categories, products = [], []
        for i in range(1, 4):
            category = Category(
                name = f'category {i}'
            )
            self.categories.append(category)

        Category.objects.bulk_create(self.categories)
        
        for i in range(1, 11):
            product = Product(
                name = f'product {i}',
                price = Decimal(f'{i}00.50'),
                quantity = i * 10,
                category = self.categories[randint(0, 2)]
            )
            products.append(product)

        Product.objects.bulk_create(products)
   
    def create_user(self):
        self.user = User.objects.create(
            username='test',
        )
        self.user.set_password('testing')
        self.user.save()

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.create_models(cls)
        cls.create_user(cls)
        cls.request = cls.client.get('/api/products')

    def test_status(self):
        self.assertEqual(self.request.status_code, 200) 

    def test_data(self):
        serializer = ProductSerializer(Product.objects.order_by('id'), many=True)
        self.assertEqual(
            self.request.data['results'],
            serializer.data
        )

    def test_create_user_without_login(self):
        post_request = self.client.post('/api/products', data = {
            'name' : 'Test Product',
            'price' : Decimal(f'{randint(1, 500)}00.50'),
            'quantity' : randint(1, 500),
            'category' : self.categories[randint(0, 2)],
        })
        self.assertEqual(post_request.status_code, 403)

    def test_create_user_with_login(self):
        self.client.login(username='test', password='testing')
        post_request = self.client.post('/api/products', data = {
            'name' : 'Test Product',
            'price' : Decimal(f'{randint(1, 500)}00.50'),
            'quantity' : randint(1, 500),
            'category' : self.categories[randint(0, 2)].id,
        }, follow=True)
        self.assertEqual(post_request.status_code, 200)
        







