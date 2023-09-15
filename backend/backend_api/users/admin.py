from django.contrib import admin
from .models import User
class UserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in User._meta.fields]

    class Meta:
        model = User
admin.site.register(User, UserAdmin)