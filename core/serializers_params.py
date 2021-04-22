from rest_framework import serializers


class CityGetByNameParamSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=64, required=True)
