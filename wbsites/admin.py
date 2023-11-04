from django.contrib import admin

from .models import EquipmentCategory, Products, Transactions

class EquipmentCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'date_created')
    
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'product_name', 'unit_price', 'sale_price', 'available_stock', 'unit_measure', 'date_updated')
    
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'transaction_type', 'stock_taken', 'transaction_amount', 'transaction_date')

admin.site.register(EquipmentCategory, EquipmentCategoryAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Transactions, TransactionsAdmin)
