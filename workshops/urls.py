from django.urls import path

from .views import WorkshopDetail

urlpatterns = [
    path("", WorkshopDetail.as_view(), name='workshop'),
]
