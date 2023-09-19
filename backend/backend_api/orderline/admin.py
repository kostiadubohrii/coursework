from django.contrib import admin
from orderline.models import *

class OrderlineAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OrderLine._meta.fields]

    class Meta:
        model = OrderLine
admin.site.register(OrderLine, OrderlineAdmin)