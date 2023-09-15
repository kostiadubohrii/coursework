from django.contrib import admin
from orders.models import *

class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]

    class Meta:
        model = Order
admin.site.register(Order, OrderAdmin)