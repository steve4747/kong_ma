#APP_orderMV/urls.py

from django.urls import path
from .views import PriceTableList, PriceTableDetail, ProductList, ProductDetail, OrderMainList, OrderMainDetail, OrderAllList, OrderAllDetail

app_name='APP_orderMV'

urlpatterns = [
    path('Pricetable/', PriceTableList.as_view()),
    path('Pricetable/<int:pk>/', PriceTableDetail.as_view()),
    path('Product/', ProductList.as_view()),
    path('Product/<int:pk>/', ProductDetail.as_view()),
    path('OrderMain/', OrderMainList.as_view()),
    path('OrderMain/<int:pk>/', OrderMainDetail.as_view()),
    path('OrderAll/', OrderAllList.as_view()),
    path('OrderAll/<int:pk>/', OrderAllDetail.as_view()),    
]
