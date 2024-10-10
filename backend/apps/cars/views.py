from django.utils.decorators import method_decorator

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticated

from drf_yasg.utils import swagger_auto_schema

from apps.cars.models import CarModel
from apps.cars.serializer import CarPhotoSerializer, CarSerializer


@method_decorator(name='get', decorator=swagger_auto_schema(security=[]))
class CarListCreateView(ListCreateAPIView):
    """
        Show all cars
    """
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    permission_classes = (AllowAny,)


@method_decorator(name='get', decorator=swagger_auto_schema(security=[]))
@method_decorator(name='put', decorator=swagger_auto_schema(security=[]))
@method_decorator(name='patch', decorator=swagger_auto_schema(security=[]))
@method_decorator(name='delete', decorator=swagger_auto_schema(security=[]))
class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
        get:
            Get car by id
        put:
            Full Update car by id
        patch:
            Partial Update car by id
        delete:
            Delete car by id
    """
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()


class CarAddPhotoView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CarPhotoSerializer
    queryset = CarModel.objects.all()
    http_method_names = ('put',)

    def perform_update(self, serializer):
        car = self.get_object()
        car.photo.delete()
        super().perform_update(serializer)
