from backend.Api.serializers.categories import CategorySerializer
from backend.categories import Category
from ..actions.objects.categories import category_filters
from Fast.django.api.views.filter import FilterView
from rest_framework import generics
from Fast.django.decorators.cache.api import control_cache_page, global_cache_page
from django.utils.decorators import method_decorator


class CategoryCreateAndListView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    @method_decorator(global_cache_page(10))
    def get(self, request, pk):
        return super().get(request, pk)


class FilterCategoryView(FilterView):
    serializer_class = CategorySerializer
    filter_obj = category_filters
    model = Category

    @method_decorator(global_cache_page(10))
    def get(self, request, pk):
        return super().get(request, pk)


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    @method_decorator(control_cache_page(30))
    def get(self, request, pk):
        return super().get(request, pk)