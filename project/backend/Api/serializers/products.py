from rest_framework import serializers
from backend.products import Product



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'