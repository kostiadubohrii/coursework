from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import User

# python manage.py makemigrations products
# python manage.py migrate products
# python manage.py runserver 

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
   description = models.TextField(blank=True, null=True, default="- Due to the developing, no description is added to products")
   category = models.ForeignKey(Category, blank=True, null=True, default=None, on_delete=models.SET_NULL)
   price = models.IntegerField(blank=True, null=True, default=None)
   oldPrice = models.IntegerField(blank=True, null=True, default=None)
   isApple = models.BooleanField(default=False)
   isActive = models.BooleanField(default=True)
   mainImage = models.ImageField(upload_to='Images/', default='Images/None/No0img.jpg')
   meanReview = models.FloatField(blank=False, null=False, default=0)
   created_at = models.DateTimeField(auto_now_add=True)
              
   def __str__(self):
      return "%s" % self.name
   class Meta:
      verbose_name = 'Product'
      verbose_name_plural = 'Products'

class ProductImage(models.Model):
   product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
   image = models.ImageField(upload_to='products_images/')
   is_active = models.BooleanField(default=True)

   def __str__(self):
      return "%s" % self.id

   class Meta:
      verbose_name = 'Image'
      verbose_name_plural = 'Images'

class ProductLogo(models.Model):
   logo = models.ImageField(upload_to='products_logos/', blank=True, null=True)
   product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
   is_active = models.BooleanField(default=True)

   def __str__(self):
      return "%s" % self.id

   class Meta:
      verbose_name = 'Logo'
      verbose_name_plural = 'Logos'


class Reviews(models.Model):
   product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
   user = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)
   review = models.FloatField(blank=True, null=True, default=None)
   posted_on = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return "User: %s, Product: %s, Review: %s" % (self.user, self.product, self.review)
   class Meta:
      verbose_name = 'Review'
      verbose_name_plural = 'Reviews'


class ReviewLine(models.Model):
   product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
   meanReview = models.FloatField(blank=True, null=True, default=None)

   def __str__(self):
       return "ReviewLine: %s, Product: %s, MeanReview: %s" % (self.id, self.product, self.meanReview)
   class Meta:
      verbose_name = 'Review Line'
      verbose_name_plural = 'Review Lines'