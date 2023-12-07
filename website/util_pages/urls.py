from django.urls import path

from .views import About, Contacts, Confidential, Terms, Questions


app_name = 'util_pages'

urlpatterns = [
    path('about/', About.as_view(), name='about'),
    path('contacts/', Contacts.as_view(), name='contacts'),
    path('confidential/', Confidential.as_view(), name='confidential'),
    path('terms-and-conditions/', Terms.as_view(), name='terms'),
    path('questions/', Questions.as_view(), name='questions'),
]
