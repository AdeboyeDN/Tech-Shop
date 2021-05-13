from django.contrib import admin
from .models import product

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name".replace(' ','-'), )}
admin.site.register(product, ProductAdmin)


