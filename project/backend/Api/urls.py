from django.urls import path

from .views.categories import CategoryCreateAndListView, CategoryDetailView
from .views.products import ProductCreateAndListView, ProductDetailView


urlpatterns = [
    path('products', ProductCreateAndListView.as_view()),
    path('products/<int:pk>', ProductDetailView.as_view()),
    path('categories', CategoryCreateAndListView.as_view()),
    path('categories/<int:pk>', CategoryDetailView.as_view()),
]
