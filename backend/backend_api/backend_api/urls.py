from django.contrib import admin
from django.urls import path
from django.urls import re_path as url

from users.views import users_list, user_detail
from products.views import products_list, product_detail, product_review_list, product_reviews_detail
from orders.views import orders_list, order_detail, order_and_orderline_spread
from orderline.views import orderLines_list, orderLine_detail, product_statistics, years
from backend_api import views

# Come import to enable usavility of the images in API.
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/users/', users_list),
    path('api/v1/users/<int:id>/', user_detail),

    path('api/v1/products/', products_list),
    path('api/v1/products/<int:id>', product_detail),

    # path('api/v1/orders/', orders_list),
    # path('api/v1/orders/<int:id>', order_detail),

    # path('api/v1/orderline/', orderLines_list),
    # path('api/v1/orderline/<int:id>', orderLine_detail),

    path('api/v1/orders/', order_and_orderline_spread),

    path('api/v1/products/reviews/', product_review_list),
    path('api/v1/products/reviews/<int:id>', product_reviews_detail), 

    path('api/v1/statistics/', product_statistics),
    path('api/v1/years/', years)


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
