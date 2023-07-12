from django.db import models

class User(models.Model):
    name = models.CharField(max_length=210, default=None)
    last_name= models.CharField(max_length=210, default=None)
    is_loggedin = models.BooleanField(default=False)
    email = models.EmailField(max_length = 254, default=None)
    password = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.name