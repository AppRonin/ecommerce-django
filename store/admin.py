from django.contrib import admin
from .models import Product

# Custom Product Admin
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'get_categories', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('name',)}

    def get_categories(self, obj):
        return ", ".join(category.name for category in obj.category.all())
    
    get_categories.short_description = "Categories"

admin.site.register(Product, ProductAdmin)