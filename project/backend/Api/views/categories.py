from Fast.django.decorators.cache.controler import renew_global_cache
from backend.Api.serializers.categories import CategorySerializer
from backend.categories import Category
from ..actions.objects.categories import category_filters
from Fast.django.api.views.filter import FilterView
from rest_framework import generics
from Fast.django.decorators.cache.api import control_cache_page, global_cache_page, static_page
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.core.cache import cache
from Fast.utils.worker import renew



class CategoryCreateAndListView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.order_by('id')
    permission_classes = IsAuthenticatedOrReadOnly,

    @method_decorator(global_cache_page(10))
    def get(self, request):
        return super().get(request)

    def post(self, request):
        super().post(request)
        return redirect(request.get_full_path())


class FilterCategoryView(FilterView):
    permission_classes = IsAuthenticatedOrReadOnly,
    serializer_class = CategorySerializer
    filter_obj = category_filters
    model = Category

    @method_decorator(global_cache_page(10))
    def get(self, request):
        return super().get(request)


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.order_by('id')
    permission_classes = IsAuthenticated,

    @method_decorator(static_page)
    def get(self, request, pk):
        return super().get(request, pk)

    def put(self, request, pk):
        renew_global_cache(request.get_full_path())
        return super().put(request, pk)

    def delete(self, request, pk):
        renew_global_cache(request.get_full_path())
        return super().delete(request, pk)