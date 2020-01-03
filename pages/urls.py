from django.urls import path

from .views import Home, contact

urlpatterns = [
    path("", Home.as_view(), name='home'),
    path("contact", contact, name='contact'),
]
