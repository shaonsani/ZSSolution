from django.urls import path
from account.views import UserRegister

urlpatterns = [
    path('register', UserRegister.as_view()),
]