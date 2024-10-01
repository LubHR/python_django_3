from django.urls import include, path

urlpatterns = [
 path('cars',include('apps.cars.urls')),
]
