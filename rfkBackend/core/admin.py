from django.contrib import admin
from .models import PrivateFile
# Register your models here.

class PrivateFileAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(PrivateFile, PrivateFileAdmin)