from backend.Api.serializers.categories import CategorySerializer
from backend.categories import Category
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response


class CategoryCreateAndListView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class FilterCategoryView(APIView):
    def get(self, request):
        return Response(Category.objects.all())


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()