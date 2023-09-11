from django.urls import include, path
from rest_framework import routers

from .views import CityViewSet, WeatherViewSet


router = routers.DefaultRouter()

router.register("weather", WeatherViewSet)
router.register("cities", CityViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
