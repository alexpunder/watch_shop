from django.urls import path

from .views import About, contacts, Confidential, Terms, questions


app_name = 'util_pages'

urlpatterns = [
    path('about/', About.as_view(), name='about'),
    path('contacts/', contacts, name='contacts'),
    path('confidential/', Confidential.as_view(), name='confidential'),
    path('terms-and-conditions/', Terms.as_view(), name='terms'),
    path('questions/', questions, name='questions'),
]
