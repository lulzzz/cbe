from rest_framework import serializers

from cbe.utils.serializer_fields import TypeField
from cbe.location.models import UrbanPropertyAddress, UrbanPropertySubAddress, RuralPropertyAddress, PoBoxAddress, AbsoluteLocalLocation, Country, City, AbsoluteLocalLocation


class CitySerializer(serializers.HyperlinkedModelSerializer):
    type = TypeField()

    class Meta:
        model = City
        fields = ('type', 'url', 'code', 'name', 'country')


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    type = TypeField()

    class Meta:
        model = Country
        fields = ('type', 'url', 'code', 'name')


class UrbanPropertyAddressSerializer(serializers.HyperlinkedModelSerializer):
    type = TypeField()

    class Meta:
        model = UrbanPropertyAddress
        fields = ('type', 'url', 'country', 'city', 'state_or_province', 'locality', 'postcode', 'street_name', 'street_number_first',
                  'street_number_first_suffix', 'street_number_last', 'street_number_last_suffix', 'street_suffix', 'street_type')


class PoBoxAddressSerializer(serializers.HyperlinkedModelSerializer):
    type = TypeField()

    class Meta:
        model = PoBoxAddress
        fields = ('type', 'url', 'country', 'city',
                  'state_or_province', 'locality', 'box_number',)


class AbsoluteLocalLocationSerializer(serializers.HyperlinkedModelSerializer):
    type = TypeField()

    class Meta:
        model = AbsoluteLocalLocation
        fields = ('type', 'url', 'name', 'x', 'y', 'z', )