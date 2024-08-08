from django.urls import path
from . import views


urlpatterns = [
    path('code/', views.SendAuthCodeAPIView.as_view(), name='sends_code'),
]