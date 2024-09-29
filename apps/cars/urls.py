from django.urls import path,include
from .views import CarListCreateView
urlpatterns = [
    path('',CarListCreateView.as_view(),name='car_list_create'),
]