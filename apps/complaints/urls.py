from django.urls import path
from . import views


urlpatterns = [
    path('', views.ComplaintCreateAPIView.as_view(), name='complaints_create'),
]