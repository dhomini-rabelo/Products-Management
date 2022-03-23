from django.db.models import (Model, CharField, DateTimeField, TextField, EmailField, ForeignKey, PositiveIntegerField, ImageField, RESTRICT, DecimalField, DateField, BooleanField, CASCADE)
from backend.categories import Category




class Product(Model):
    name = CharField(max_length=256)
    price = DecimalField(decimal_places=2, max_digits=20)
    quantity = PositiveIntegerField()
    category = ForeignKey(Category, on_delete=CASCADE)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self):
        return self.name.upper()
