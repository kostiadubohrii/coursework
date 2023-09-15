from django.db import models
from products.models import Product
from orders.models import Order

# py manage.py makemigrations options
# py manage.py migrate options
# py manage.py runserver

class Option(models.Model):
    optionId = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, blank=False, default=None, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, blank=False, default=None, on_delete=models.PROTECT)
    quantity = models.IntegerField(blank=False, null=True, default=1)
    totalPrice = models.FloatField(blank=False, null=False, default=None)

    def __str__(self):
        return "Option ID: %s | Product: %s" % (self.order, self.product)
    
    class Meta:
      verbose_name = 'Option'
      verbose_name_plural = 'Options' 