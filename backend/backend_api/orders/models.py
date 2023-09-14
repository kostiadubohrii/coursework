from django.db import models
from products.models import Product
from users.models import User

# py manage.py makemigrations
# py manage.py migrate 
# py manage.py runserver


class Order(models.Model):
    orderId = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, blank=False, default=None, on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=False, default=None, on_delete=models.CASCADE)
    orderOn = models.DateField(blank=False, null=True, default=None)
    items = models.IntegerField(blank=False, null=True, default=1)
    totalPrice = models.FloatField(blank=False, null=True, default=None)

    def __str__(self):
        return "Order ID: %s | Product: %s" % (self.orderId, self.product)
    
    class Meta:
      verbose_name = 'Order'
      verbose_name_plural = 'Orders' 