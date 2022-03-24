from Fast.django.decorators.cache.api import control_cache_page, global_cache_page
from backend.Api.serializers.products import ProductSerializer
from backend.products import Product
from Fast.django.api.views.filter import FilterView
from ..actions.objects.products import product_filters
from rest_framework import generics
from django.utils.decorators import method_decorator




class ProductCreateAndListView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    @method_decorator(global_cache_page(10))
    def get(self, request, pk):
        return super().get(request, pk)


class FilterProductView(FilterView):
    serializer_class = ProductSerializer
    filter_obj = product_filters
    model = Product

    @method_decorator(global_cache_page(10))
    def get(self, request, pk):
        return super().get(request, pk)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    @method_decorator(control_cache_page(30))
    def get(self, request, pk):
        return super().get(request, pk)
        
