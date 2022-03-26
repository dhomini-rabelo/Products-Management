from django.test import TestCase
from backend.accounts.app.models import User
from backend.products.app.models import Product
from backend.categories.app.models import Category
from decimal import Decimal
from random import randint


class TestModelDataListApi(TestCase):

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