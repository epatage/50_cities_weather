from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("api.openweathermap.org/data/2.5/", include("api.urls")),
    path("api/", include("api.urls")),
    path("admin/", admin.site.urls),
]
