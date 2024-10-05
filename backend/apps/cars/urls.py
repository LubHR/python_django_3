from django.urls import path

from .views import CarAddPhotoView, CarListCreateView

urlpatterns = [
    path('', CarListCreateView.as_view(), name='car_list_create'),
    path('/<int:pk>/photos', CarAddPhotoView.as_view(), name='car_photos'),
]
