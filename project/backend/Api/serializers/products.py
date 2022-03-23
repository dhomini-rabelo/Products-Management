from backend.Api.serializers.categories import CategorySerializer
from rest_framework import serializers
from backend.products import Product



class ProductSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        representation = super(ProductSerializer, self).to_representation(instance)
        representation['category'] = instance.category.name
        return representation

    class Meta:
        model = Product
        fields = 'id', 'name', 'price', 'quantity', 'category', 'created', 'updated'