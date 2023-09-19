from django.db import models
from users.models import User

# py manage.py makemigrations
# py manage.py migrate 
# py manage.py runserver


class Order(models.Model):
    orderId = models.AutoField(primary_key=True)
    userId = models.ForeignKey(User, blank=False, default=None, on_delete=models.PROTECT)
    orderOn = models.DateField(blank=False, null=True, default=None)

    def __str__(self):
        return "Order ID: %s | Product: %s" % (self.orderId, self.userId)
    
    class Meta:
      verbose_name = 'Order'
      verbose_name_plural = 'Orders' 