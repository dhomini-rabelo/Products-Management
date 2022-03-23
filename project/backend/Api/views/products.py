from backend.Api.serializers.products import ProductSerializer
from backend.products import Product
from rest_framework import generics



class ProductCreateAndListView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()



class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()