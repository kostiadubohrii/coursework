from django.db import models
from products.models import Product
from orders.models import Order

# py manage.py makemigrations orderline
# py manage.py migrate orderline
# py manage.py runserver

class OrderLine(models.Model):
    orderLineId = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, blank=False, default=None, on_delete=models.PROTECT)
    orderId = models.ForeignKey(Order, blank=False, default=None, on_delete=models.PROTECT)
    quantity = models.IntegerField(blank=False, null=True, default=1)
    totalPrice = models.FloatField(blank=False, null=False, default=None)

    def __str__(self):
        return "OrderLine ID: %s | Product: %s" % (self.orderId, self.product)
    
    class Meta:
      verbose_name = 'OrderLine'
      verbose_name_plural = 'OrderLines' 