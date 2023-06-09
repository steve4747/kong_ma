#APP_orderMV/serializers.py

from rest_framework import serializers 
from .models import Price_table, Product, Order_main, Order_all

class PriceTableSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('__all__')  #('tp', 'num', 'name', 'price',) 
        model = Price_table

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('__all__')  
        model = Product
        
class OrderMainSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('__all__')
        model = Order_main
        
class OrderAllSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('__all__')
        model = Order_all