from django.contrib import admin

# Register your models here.
from .models import Price_table, Product, Order_main, Order_all

admin.site.register(Price_table)
admin.site.register(Product)
admin.site.register(Order_main)
admin.site.register(Order_all)
