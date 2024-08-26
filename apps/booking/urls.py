from django.urls import path
from . import views


urlpatterns = [
    path('', views.BookingCreateAPIView.as_view(), name='add_booking'),
]