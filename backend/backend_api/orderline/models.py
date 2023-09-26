from django.db import models
from products.models import Product
from orders.models import Order

# py manage.py makemigrations orderline
# py manage.py migrate orderline
# py manage.py runserver

class OrderLine(models.Model):
    orderLineId = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    orderId = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False, null=True, default=1)
    totalPrice = models.FloatField(blank=False, null=False, default=None)

    def __str__(self):
        return "OrderLine ID: %s | Product: %s" % (self.orderId, self.product)
    
    class Meta:
      verbose_name = 'OrderLine'
      verbose_name_plural = 'OrderLines' 

class OrderLineProduct(models.Model):
    product_text = models.ForeignKey(Product, blank=False, null=True, default=None, on_delete=models.CASCADE)
    orderline = models.ForeignKey(OrderLine, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return "OrderLine product: %s " % (self.id)
    
    class Meta:
        verbose_name = "OrderLine product"
        verbose_name_plural = "OrderLine products"
