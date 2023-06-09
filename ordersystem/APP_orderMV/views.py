from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from APP_orderMV.models import Price_table, Product, Order_main, Order_all
from .serializers import PriceTableSerializer, ProductSerializer, OrderMainSerializer, OrderAllSerializer

# Create your views here.

def home(request):
    priceTable = Price_table.object.all()
    return render(request, 'home.html', {
        'price_table': priceTable,
    })


class PriceTableList(generics.ListCreateAPIView): 
    queryset = Price_table.objects.all() 
    serializer_class = PriceTableSerializer

class PriceTableDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Price_table.objects.all() 
    serializer_class = PriceTableSerializer

class ProductList(generics.ListCreateAPIView): 
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer

class OrderMainList(generics.ListCreateAPIView): 
    queryset = Order_main.objects.all() 
    serializer_class = OrderMainSerializer

class OrderMainDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Order_main.objects.all() 
    serializer_class = OrderMainSerializer

class OrderAllList(generics.ListCreateAPIView): 
    queryset = Order_all.objects.all() 
    serializer_class = OrderAllSerializer

class OrderAllDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Order_all.objects.all() 
    serializer_class = OrderAllSerializer















