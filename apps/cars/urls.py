from django.urls import path
from . import views


urlpatterns = [
    path('', views.UserCarCreateListView.as_view(), name='user_car'),
    path('<int:pk>/', views.UserCarRetrieveUpdateDestroyAPIView.as_view(), name='user_car_retrieve_update_destroy'),
]