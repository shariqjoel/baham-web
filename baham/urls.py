from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_home, name='home'),
    path('baham/vehicles', views.view_vehicles, name='vehicles'),
    path('baham/vehicles/create', views.create_vehicle, name='createvehicle'),
    path('baham/vehicles/save/', views.save_vehicle, name='savevehicle'),
    path('baham/vehicles/<int:model_id>/void/', views.void_vehicle_model, name='void_vehicle_model'),
    path('baham/vehicles/<int:model_id>/unvoid/', views.unvoid_vehicle_model, name='unvoid_vehicle_model'),
    path('baham/aboutus', views.view_aboutus, name='aboutus'),
    
]
