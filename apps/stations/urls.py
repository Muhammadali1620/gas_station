from django.urls import path
from . import views


urlpatterns = [
    path('', views.StationListAPIView.as_view(), name='station_list'),
]