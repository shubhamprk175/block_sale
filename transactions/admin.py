from django.contrib import admin
from .models import Transaction
# Register your models here.

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'amount', 'seller', 'buyer')
    list_display_links = ('id', 'product_name')
    search_fields = ('product_name',)
    list_per_page = 25


# Register your models here.
admin.site.register(Transaction, TransactionAdmin)
