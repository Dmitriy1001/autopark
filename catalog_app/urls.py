from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path('drivers/driver/', views.DriverList.as_view()),
    path('drivers/driver/<int:driver_id>/', views.DriverDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)