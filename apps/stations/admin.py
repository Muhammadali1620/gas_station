from django.contrib import admin
from apps.stations.models import Station


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'slug']
    list_display_links = list_display
    prepopulated_fields = {'slug':['name']}
