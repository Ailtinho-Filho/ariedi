from django.urls import path

from .views import WorkshopDetail

urlpatterns = [
    path("<pk>", WorkshopDetail.as_view(), name='workshop'),
]
