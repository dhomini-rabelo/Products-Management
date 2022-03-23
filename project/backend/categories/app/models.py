from django.db.models import (Model, CharField, DateTimeField, TextField, EmailField, ForeignKey, PositiveIntegerField, ImageField, RESTRICT, DecimalField, DateField, BooleanField)



class Category(Model):
    name = CharField(max_length=256)
    created = DateTimeField(auto_now_add=True)
