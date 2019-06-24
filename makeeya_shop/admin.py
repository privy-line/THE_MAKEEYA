from django.contrib import admin
 
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'initial_price','current_price', 'stock', 'available', 'created_at', 'expires_at']
    list_filter = ['available', 'created_at', 'expires_at' ]
    list_editable = ['current_price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)

# Register your models here.
