from django.urls import path
from . import views


urlpatterns = [
    #Register
    path('register/send_code/', views.RegisterSendCodeAPIView.as_view(), name='register_send_code'),
    path('register/', views.RegisterAPIView.as_view(), name='register'),

    path('verify_code/', views.VerifyCodeAPIView.as_view(), name='verify_code'),

    #login
    path('login/', views.LoginAPIView.as_view(), name='login'),

    #Change password
    path('change_password/', views.ChangePasswordAPIView.as_view(), name='change_password'),
    path('change_password/send_code/', views.SendChangePasswordCodeAPIView.as_view(), name='send_code_for_change_password'),
]