from django.urls import path
from . import views


urlpatterns = [
    path('', views.WishlistListAPIView.as_view(), name='wishlist'),
    path('<int:pk>/', views.WishlistCreateOrDelateAPIView.as_view(), name='create_or_delate_wishlist'),
]