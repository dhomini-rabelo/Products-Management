from django.apps import AppConfig


class CategoriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.categories.app'
    verbose_name = 'categories'
    label = 'categories'
