from backend.Api.serializers.products import ProductSerializer
from backend.products import Product
from Fast.django.api.views.filter import FilterView
from ..actions.objects.products import product_filters
from rest_framework import generics





class ProductCreateAndListView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class FilterProductView(FilterView):
    serializer_class = ProductSerializer
    filter_obj = product_filters
    model = Product


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()