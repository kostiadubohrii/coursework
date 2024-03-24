from django.db import models
from django import forms

#python manage.py makemigrations users
#python manage.py migrate users
class User(models.Model):
    name = models.CharField(max_length=210, null=False, default="")
    lastName= models.CharField(max_length=210, null=False, default="")
    isOnline = models.BooleanField(default=False)
    email = models.EmailField(max_length=200, default='')
    password = models.CharField(max_length=200, null=False, blank=False, default=None)

    def __str__(self):
        return "ID: " + str(self.id) + ', User: ' + self.name + ' '+ self.lastName