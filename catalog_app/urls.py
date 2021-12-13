from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path('drivers/driver/', views.DriverList.as_view()),
    path('drivers/driver/<int:driver_id>/', views.DriverDetail.as_view()),
    path('vehicles/vehicle/', views.VehicleList.as_view()),
    path('vehicles/vehicle/<int:vehicle_id>/', views.VehicleDetail.as_view()),
    path('vehicles/set_driver/<int:vehicle_id>/', views.VehicleSetDriver.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
