from django.contrib import admin
from .models import Product




admin.site.empty_value_display = 'NULL'



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'name', 'price', 'quantity'
    list_display_links = 'name',
    list_per_page = 50
    list_select_related = 'category',
    ordering = 'name',
    search_fields = 'name',
