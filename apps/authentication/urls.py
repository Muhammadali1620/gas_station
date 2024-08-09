from django.urls import path
from . import views


urlpatterns = [
    path('code/', views.SendAuthCodeAPIView.as_view(), name='sends_code'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
]