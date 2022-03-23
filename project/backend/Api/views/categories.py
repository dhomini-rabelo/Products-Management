from backend.Api.serializers.categories import CategorySerializer
from backend.categories import Category
from rest_framework import generics



class CategoryCreateAndListView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()



class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()