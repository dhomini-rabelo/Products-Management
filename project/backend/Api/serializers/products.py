from rest_framework import serializers
from backend.products import Product



class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'