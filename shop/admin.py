from django.contrib import admin
from shop.models import Product
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('price','name','desc')