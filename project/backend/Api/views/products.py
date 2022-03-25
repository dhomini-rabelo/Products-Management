from Fast.django.decorators.cache.api import control_cache_page, global_cache_page
from backend.Api.serializers.products import ProductSerializer
from backend.products import Product
from Fast.django.api.views.filter import FilterView
from backend.products.actions.app.renew_product import renew_product_api
from ..actions.objects.products import product_filters
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.core.cache import cache
from Fast.utils.worker import renew


class ProductCreateAndListView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.order_by('id')
    permission_classes = IsAuthenticatedOrReadOnly,

    @method_decorator(global_cache_page(10))
    def get(self, request):
        return super().get(request)

    def post(self, request):
        super().post(request)
        return redirect(request.get_full_path())


class FilterProductView(FilterView):
    permission_classes = IsAuthenticatedOrReadOnly,
    serializer_class = ProductSerializer
    filter_obj = product_filters
    model = Product

    @method_decorator(global_cache_page(10))
    def get(self, request):
        return super().get(request)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.order_by('id')
    permission_classes = IsAuthenticated,

    @method_decorator(control_cache_page(5))
    def get(self, request, pk):
        return super().get(request, pk)

    def put(self, request, pk):
        response = super().put(request, pk)
        renew(request.get_full_path())
        return response

    def delete(self, request, pk):
        response = super().delete(request, pk)
        cache.set(request.get_full_path(), None, None)
        return response
    
        
