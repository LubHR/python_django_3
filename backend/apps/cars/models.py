from django.db import models

from core.models import BaseModel

from apps.cars.managers import CarManager
from apps.cars.services import upload_car_photo


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'

    model = models.CharField(max_length=200)
    year = models.IntegerField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to=upload_car_photo, blank=True)

    objects = CarManager()
