from django.contrib import admin

# Register your models here.
from .models import Products, Order_main, Order_all #Price_table, 

#admin.site.register(Price_table)
admin.site.register(Products)
admin.site.register(Order_main)
admin.site.register(Order_all)
