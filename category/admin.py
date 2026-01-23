from django.contrib import admin
from .models import Category

# Custom Category Admin
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')

admin.site.register(Category, CategoryAdmin)