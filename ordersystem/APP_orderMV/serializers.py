#APP_orderMV/serializers.py

from rest_framework import serializers 
from .models import Products, Order_main, Order_all #Price_table, 

class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('__all__')  
        model = Products
        
class OrderMainSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('__all__')
        model = Order_main
        
class OrderAllSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('__all__')
        model = Order_all