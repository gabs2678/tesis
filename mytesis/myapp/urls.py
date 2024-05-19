# myapp/urls.py

from django.urls import path
from .views import hello_world  # make sure to import your view

urlpatterns = [
    path('hello/', hello_world, name='hello-world'),
]
