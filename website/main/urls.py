from django.urls import path

from .views import homepage, sell_watches


app_name = 'main'

urlpatterns = [
    path('', homepage, name='homepage'),
    path('sell_watches/', sell_watches, name='sell_watches'),
]
