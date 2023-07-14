from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# python manage.py makemigrations product
# python manage.py migrate product
class Category(models.Model):
   category = models.CharField(max_length=86, blank=True, null=True, default=None,)
   is_active = models.BooleanField(default=True)
   is_visible = models.BooleanField(default=False)

   def __str__(self):
      return "%s" % self.category

   class Meta:
      verbose_name = 'Category name'
      verbose_name_plural = 'Category names'

class Product(models.Model):
   name = models.CharField(max_length=64, blank=True, null=True, default=None)
   description = models.TextField(blank=True, null=True, default=None)
   price = models.IntegerField(blank=True, null=True, default=None)
   old_price = models.IntegerField(blank=True, null=True, default=None)
   is_apple = models.BooleanField(default=False)
   is_active = models.BooleanField(default=True)
   category = models.ForeignKey(Category, blank=True, null=True, default=None, on_delete=models.CASCADE)
   review = models.FloatField(blank=True, null=True, default=None,
                              validators = [MinValueValidator(0.0), MaxValueValidator(5.0)],
                              )
   def __str__(self):
      return "%s" % self.name
   class Meta:
      verbose_name = 'Product'
      verbose_name_plural = 'Products'

class ProductImage(models.Model):
   product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
   image = models.ImageField(upload_to='products_images/')
   is_active = models.BooleanField(default=True)
   is_main = models.BooleanField(default=False)

   def __str__(self):
      return "%s" % self.id

   class Meta:
      verbose_name = 'Image'
      verbose_name_plural = 'Images'

class ProductLogo(models.Model):
   product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
   logo = models.ImageField(upload_to='products_logos/', blank=True, null=True)
   is_active = models.BooleanField(default=True)

   def __str__(self):
      return "%s" % self.id

   class Meta:
      verbose_name = 'Logo'
      verbose_name_plural = 'Logos'