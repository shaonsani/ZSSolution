from country.models import Country, State
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
