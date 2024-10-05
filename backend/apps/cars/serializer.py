from rest_framework import serializers

from apps.cars.models import CarModel


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    model = serializers.CharField(max_length=50)
    year = serializers.IntegerField()
    price = serializers.IntegerField()


class CarPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('photo',)
        extra_kwargs = {'photo': {'required': True}}
