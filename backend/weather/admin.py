from django.contrib import admin
from .models import Weather


@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    list_display = (
        'city',
        'dt',
        'temp',
        'pressure',
        'humidity',
    )
    search_fields = ("city",)
    list_filter = ("city",)
    empty_value_display = "-пусто-"
