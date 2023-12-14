from django.urls import path

from .views import watch_detail, watch_list, cart_add, cart_remove, cart_detail


app_name = 'shop'

urlpatterns = [
    path('watch/', watch_list, name='watch_list'),
    path('watch/<int:pk>/', watch_detail, name='watch_detail'),
    path('cart/add/<int:pk>/', cart_add, name='cart_add'),
    path('cart/remove/<int:pk>/', cart_remove, name='cart_remove'),
    path('cart/', cart_detail, name='cart_detail'),
]
