from django.db import models


#python manage.py makemigrations users
#python manage.py migrate users
class User(models.Model):
    name = models.CharField(max_length=210, null=True, default=None)
    lastName= models.CharField(max_length=210, null=True, default=None)
    isLoggedIn = models.BooleanField(default=False)
    email = models.EmailField(max_length=200, default='')
    password = models.CharField(max_length=200, null=True)
    

    def __str__(self):
        return "ID: " + str(self.id) + ', User: ' + self.name + ' '+ self.lastName