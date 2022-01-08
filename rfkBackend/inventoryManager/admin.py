from django.contrib import admin

from .models import Product, Merch, ProductCount, TotalProductCount, ProductReplenishment

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'active')


class MerchAdmin(admin.ModelAdmin):
    list_display = ('name','amount', 'price')

class ProductCountAdmin(admin.ModelAdmin):
    list_display = ('product', 'amount')

class TotalProductCountAdmin(admin.ModelAdmin):
    list_display = ('date', 'author')

class ProductReplenishmentAdmin(admin.ModelAdmin):
    list_display = ('date', 'author')

admin.site.register(TotalProductCount, TotalProductCountAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Merch, MerchAdmin)
admin.site.register(ProductCount, ProductCountAdmin)
admin.site.register(ProductReplenishment, ProductReplenishmentAdmin)
