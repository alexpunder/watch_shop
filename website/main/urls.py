from django.urls import path

from .views import (
    homepage, sell_watches, evaluation, services, popup_message, buy_watch
)


app_name = 'main'

urlpatterns = [
    path('', homepage, name='homepage'),
    path('sell_watches/', sell_watches, name='sell_watches'),
    path('buy_watch/', buy_watch, name='buy_watch'),
    path('evaluation/', evaluation, name='evaluation'),
    path('services/', services, name='services'),
    path('popup_message/', popup_message, name='popup_message')
]
