from django.urls import path
from country.views import CountryAPI, StateAPI, AddressAPI

urlpatterns = [
    path('countries', CountryAPI.as_view(), name='country_list'),
    path('states', StateAPI.as_view(), name='state_list'),
    path('address', AddressAPI.as_view(), name='address_list'),
]