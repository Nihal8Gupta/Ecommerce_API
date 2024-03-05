from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','description','price','image_url']

@admin.register(CartItem)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id','product_id','quantity']