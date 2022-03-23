from django.contrib import admin
from .models import Category



admin.site.empty_value_display = 'NULL'



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name', 'created'
    list_display_links = 'name',
    list_per_page = 50
    ordering = 'name',
    search_fields = 'name',