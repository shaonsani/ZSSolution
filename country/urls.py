from django.urls import path
from country.views import CountryAPI

urlpatterns = [
    path('countries', CountryAPI.as_view(), name='country_list'),
]
