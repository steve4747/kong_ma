from django.db import models

# Create your models here.

class Products(models.Model):
    TYPE_CHOICES = [
		('0', '單點主餐'),
		('1', '便當'),
		('2', '湯品'),
		('3', '小菜類'),
        ('4', '飲料類')
	]
    prod_type = models.CharField(max_length=5, choices=TYPE_CHOICES)
    prod_no = models.CharField(max_length=5)
    prod_id = models.CharField(max_length=10, editable=False)
    prod_name = models.CharField(max_length=30)
    prod_price = models.IntegerField()
    
    def save(self, *args, **kwargs):
        self.prod_id = self.prod_type + self.prod_no
        super(Products, self).save(self, *args, **kwargs)
        
    def __str__(self):
        return '類別:{} 序號:{} 品項ID:{} 品名:{} 價格:{}'.format(self.prod_type, self.prod_no, self.prod_id, self.prod_name, self.prod_price)


class Order_main(models.Model):
    STATE_CHOICES = [
		('0', '內用'),
		('1', '外帶')
	]
    created_at = models.DateTimeField(auto_now_add=True)
    order_price = models.IntegerField()
    order_state = models.CharField(max_length = 10, choices = STATE_CHOICES)
    
    def __str__(self):
        return '訂餐時間:{} 訂單金額:{} 用餐狀態:{}'.format(self.created_at, self.order_price, self.order_state)

class Order_all(models.Model):
    each_order_id= models.ForeignKey('Order_main', on_delete=models.CASCADE, related_name='Order_ID')
    created_at = models.DateTimeField(auto_now_add=True)
    pid = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='prod_ID')
    quantity = models.IntegerField()
    subtotal = models.IntegerField()
    
    def __str__(self):
        return '訂單編號:{} 訂餐時間:{} 品項ID:{} 數量:{} 小計:{}'.format(self.order_id, self.created_at, self.pid, self.quantity, self.subtotal)