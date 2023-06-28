#APP_orderMV/urls.py

from django.urls import path
from .views import ProductsList, ProductsDetail, OrderMainList, OrderMainDetail, OrderAllList, OrderAllDetail #PriceTableList, PriceTableDetail, 

app_name='APP_orderMV'

urlpatterns = [
    #path('Pricetable/', PriceTableList.as_view()),
    #path('Pricetable/<int:pk>/', PriceTableDetail.as_view()),
    path('Products/', ProductsList.as_view()),
    path('Products/<int:pk>/', ProductsDetail.as_view()),
    path('OrderMain/', OrderMainList.as_view()),
    path('OrderMain/<int:pk>/', OrderMainDetail.as_view()),
    path('OrderAll/', OrderAllList.as_view()),
    path('OrderAll/<int:pk>/', OrderAllDetail.as_view()),    
]
