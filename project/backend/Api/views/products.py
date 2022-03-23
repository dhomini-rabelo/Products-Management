from backend.Api.serializers.products import ProductSerializer
from backend.products import Product
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response



class ProductCreateAndListView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class FilterProductView(APIView):
    def get(self, request):
        serializer = ProductSerializer(Product.objects.all(), many=True)
        return Response(serializer.data)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()