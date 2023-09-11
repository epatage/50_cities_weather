from django.contrib import admin
from .models import City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "country",
    )
    search_fields = ("name",)
    list_filter = ("country", "name")
    empty_value_display = "-пусто-"
