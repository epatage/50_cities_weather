from rest_framework import serializers
from weather.models import Weather
from cities.models import City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = City


class WeatherSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        fields = ("city", "temp", "pressure", "dt", 'humidity')
        model = Weather
