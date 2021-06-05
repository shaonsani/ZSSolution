from django.urls import path
from account.views import UserRegister
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register', UserRegister.as_view(), name='user_register'),
    path('login', obtain_auth_token, name='user_login'),
]