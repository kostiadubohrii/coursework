from django.contrib import admin
from django.urls import path
from users.views import users_list, user_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', users_list),
    path('users/<int:id>/', user_detail)

]
