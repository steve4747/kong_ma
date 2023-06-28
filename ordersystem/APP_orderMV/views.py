from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from APP_orderMV.models import Products, Order_main, Order_all #Price_table,
from .serializers import ProductsSerializer, OrderMainSerializer, OrderAllSerializer #PriceTableSerializer, 

# Create your views here.

def home(request):
    #priceTable = Price_table.object.all()
    return render(request, 'homepage0426.html') # , {
        #'price_table': priceTable,
    #})

class ProductsList(generics.ListCreateAPIView): 
    queryset = Products.objects.all() 
    serializer_class = ProductsSerializer

class ProductsDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Products.objects.all() 
    serializer_class = ProductsSerializer

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
    
@api_view(['POST'])
def createOrder(request):
    serializer = OrderAllSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
@api_view(['POST'])
def updateOrder(request, pk):
    order = Order_all.objects.get(id=pk)
    serializer = OrderAllSerializer(instance=order, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
@api_view(['DELETE'])
def deleteOrder(request, pk):
    order = Order_all.objects.get(id=pk)
    order.delete()
    return Response('Item succsesfully delete!')

@api_view(['GET'])
def getProducts(request):
    table = Products.objects.all()
    serializer = ProductsSerializer(instance=table, data=request.data)
    return Response(serializer.data)
       
    #getOrder, 

        















