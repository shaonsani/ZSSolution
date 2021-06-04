from django.urls import path
from country.views import CountryAPI, StateAPI

urlpatterns = [
    path('countries', CountryAPI.as_view(), name='country_list'),
    path('states', StateAPI.as_view(), name='state_list'),
]