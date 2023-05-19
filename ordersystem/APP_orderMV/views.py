from django.shortcuts import render
from django.http import HttpResponse
from .models import Price_table
# Create your views here.

#這之後的html檔應該會放上 Zion做的，而在html裡面呼叫Price_table即可?
def home(request):
    priceTable = Price_table.object.all()
    return render(request, 'home.html', {
        'price_table': priceTable,
    })
