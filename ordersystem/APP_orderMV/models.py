from django.db import models

# Create your models here.

class Price_table(models.Model):
    tp = models.CharField(max_length=5)
    num = models.CharField(max_length=5)
    name = models.CharField(max_length=30)
    price = models.IntegerField()

    def __str__(self):
        return '類別:{} 編號:{} 品項:{} 價格:{}'.format(self.tp, self.num, self.name, self.price)
    
class Product(models.Model):
    pord_id = models.ForeignKey('Price_table', on_delete=models.CASCADE) #, related_name='product_names')
    prod_nam = models.CharField(max_length=30)
    
    def __str__(self):
        return '品項ID:{} 品項:{}'.format(self.prod_id, self.prod_nam)

class Order_main(models.Model):
    order_id = models.CharField(max_length=64, primary_key=True, verbose_name='訂單編號')
    created_at = models.DateTimeField(auto_now_add=True)
    ordering = models.CharField(max_length=500)
    
    def __str__(self):
        return '訂單編號:{} 訂餐時間:{} 訂單內容:{}'.format(self.order_id, self.created_at, self.ordering)

class Order_all(models.Model):
    order_id= models.ForeignKey('Order_main', on_delete=models.CASCADE, related_name='Order_ID')
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    
    def __str__(self):
        return '訂單編號:{} 訂餐時間:{} 品項:{} 數量:{}'.format(self.order_id, self.created_at, self.name, self.quantity)