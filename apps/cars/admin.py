from django.contrib import admin
from apps.cars.models import CarModel


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent',)
    list_display_links = list_display
    prepopulated_fields = {'slug': ['name']}