from django.contrib import admin
from orderline.models import *


class OrderlineProductInline(admin.TabularInline):
    model = OrderLineProduct
    extra = 0
class OrderlineAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OrderLine._meta.fields]
    inlines = [OrderlineProductInline]

    class Meta:
        model = OrderLine
        
admin.site.register(OrderLine, OrderlineAdmin)