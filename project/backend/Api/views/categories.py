from backend.Api.serializers.categories import CategorySerializer
from backend.categories import Category
from ..actions.objects.categories import category_filters
from Fast.django.api.views.filter import FilterView
from rest_framework import generics



class CategoryCreateAndListView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class FilterCategoryView(FilterView):
    serializer_class = CategorySerializer
    filter_obj = category_filters
    model = Category


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()