from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'status', 'price', 'posted_on', 'posted_by')
    list_display_links = ('id', 'product_name')
    list_filter = ('posted_by',)
    list_editable = ('status', 'price',)
    search_fields = ('product_name',)
    list_per_page = 25


# Register your models here.
admin.site.register(Product, ProductAdmin)
