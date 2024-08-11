from django.urls import path
from . import views


urlpatterns = [
    #login
    path('code/', views.SendAuthCodeAPIView.as_view(), name='sends_code'),
    path('login/code/', views.CodeLoginAPIView.as_view(), name='code_login'),
    path('login/password/', views.PasswordLoginAPIView.as_view(), name='password_login'),

    #change password
    path('change_password/', views.ChangePasswordAPIView.as_view(), name='change_password'),
    path('change_password/send_code/', views.SendChangePasswordCodeAPIView.as_view(), name='send_code_for_change_password'),
]