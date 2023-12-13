from django.urls import path

from .views import watch_detail, watch_list


app_name = 'shop'

urlpatterns = [
    path('watch/', watch_list, name='watch_list'),
    path('watch/<int:pk>/', watch_detail, name='watch_detail'),
]
