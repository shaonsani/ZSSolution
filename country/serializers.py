from country.models import Country, State, Address
from rest_framework import serializers


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
    country = serializers.ReadOnlyField(source='country.name')

    class Meta:
        model = State
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    state = serializers.ReadOnlyField(source='state.name')

    class Meta:
        model = Address
        fields = '__all__'
