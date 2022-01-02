from django.contrib import admin

from .models import Product, Merch, ProductCount, TotalProductCount
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class MerchAdmin(admin.ModelAdmin):
    list_display = ('name','amount', 'price')

class ProductCountAdmin(admin.ModelAdmin):
    list_display = ('product', 'amount')

class TotalProductCountAdmin(admin.ModelAdmin):
    list_display = ('date', 'author')


admin.site.register(TotalProductCount, TotalProductCountAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Merch, MerchAdmin)
admin.site.register(ProductCount, ProductCountAdmin)
