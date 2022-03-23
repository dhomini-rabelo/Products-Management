from rest_framework import serializers
from backend.categories import Category



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = 'name', 'id'