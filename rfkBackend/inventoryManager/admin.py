from django.contrib import admin

from .models import Product, Merch
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class MerchAdmin(admin.ModelAdmin):
    list_display = ('name','amount', 'price')

admin.site.register(Product, ProductAdmin)
admin.site.register(Merch, MerchAdmin)