from django.contrib import admin
from options.models import *

class OptionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Option._meta.fields]

    class Meta:
        model = Option
admin.site.register(Option, OptionAdmin)