from django.contrib import admin
from django.urls import path
from users.views import users_list, user_detail
from products.views import products_list, product_detail


# Come import to enable usavility of the images in API.
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', users_list),
    path('users/<int:id>/', user_detail),
    path('products/', products_list),
    path('products/<int:id>', product_detail)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
