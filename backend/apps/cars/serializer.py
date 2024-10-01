from rest_framework import serializers


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    model = serializers.CharField(max_length=50)
    year = serializers.IntegerField()
    price = serializers.IntegerField()