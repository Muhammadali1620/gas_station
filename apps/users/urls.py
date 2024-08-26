from django.urls import path
from . import views


urlpatterns = [
    path('profile/', views.UserRetrieveUpdateAPIView.as_view(), name='user_profile'),
]