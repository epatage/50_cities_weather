from rest_framework import viewsets
from .serializers import WeatherSerializer, CitySerializer

from cities.models import City
from weather.models import Weather


class WeatherViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
