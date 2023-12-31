from django.contrib import admin
from django.urls import path
from django.urls import re_path as url

from users.views import users_list, user_detail
from products.views import products_list, product_detail, product_review_list, product_reviews_detail
from orders.views import orders_list, order_detail, order_and_orderline_spread
from orderline.views import orderLines_list, orderLine_detail
from backend_api import views

# Come import to enable usavility of the images in API.
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),

    path('users/', users_list),
    path('users/<int:id>/', user_detail),

    path('products/', products_list),
    path('products/<int:id>', product_detail),

    path('orders/', orders_list),
    path('orders/<int:id>', order_detail),

    path('orderline/', orderLines_list),
    path('orderline/<int:id>', orderLine_detail),

    path('processorder/', order_and_orderline_spread),

    path('products/reviews/', product_review_list),
    path('products/reviews/<int:id>', product_reviews_detail),

    url(r'statistics/', views.statistics, name="statistics"), 

    path('statistics_data/', views.statistics_data, name='statistics_data'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
