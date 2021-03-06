from django.contrib.contenttypes.models import ContentType

from rest_framework import serializers

from cbe.utils.serializer_fields import TypeField, GenericRelatedField
from cbe.customer.models import Customer, CustomerAccount, CustomerAccountContact
from cbe.party.models import Individual, Organisation, TelephoneNumber
from cbe.party.serializers import IndividualSerializer, OrganisationSerializer, TelephoneNumberSerializer, PartyRelatedField


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    #party = GenericRelatedField( many=False, serializer_dict={
    #        Individual: IndividualSerializer(),
    #        Organisation: OrganisationSerializer(),
    #    })
    party = PartyRelatedField()
    type = TypeField()

    class Meta:
        model = Customer
        fields = ('type', 'url', 'customer_number',
                  'customer_status', 'party', 'customeraccount_set')

    def create(self, validated_data):
        validated_data.pop('customeraccount_set')
        print( validated_data )
        return Customer.objects.create(**validated_data)



class CustomerAccountContactSerializer(serializers.HyperlinkedModelSerializer):
    type = TypeField()
    party = GenericRelatedField( many=False,
        serializer_dict={ 
            Individual: IndividualSerializer(),
            Organisation: OrganisationSerializer(),
        })

    class Meta:
        model = CustomerAccountContact
        fields = ('type', 'url', 'party', 'customeraccount_set')


class CustomerAccountSerializer(serializers.HyperlinkedModelSerializer):
    type = TypeField()

    class Meta:
        model = CustomerAccount
        fields = ('type', 'url', 'customer', 'account_number', 'account_status',
                  'account_type', 'name', 'pin', 'credit_limit', 'customer_account_contact',)


sample_json = """
{
    "type": "Customer",
    "customer_number": "512332",
    "customer_status": "Active",
    "party": {
        "type": "Organisation",
        "name": "A cool store4"
    }
}
{
    "type": "Customer",
    "customer_number": "1512332212",
    "customer_status": "Active",
    "party": {
        "type": "Organisation",
        "url": "http://127.0.0.1:8000/api/sid/common_business_entities/party/organisations/2/"
    }
}

{ "type": "Customer","customer_number": "512332","customer_status": "Active","party": { "url":"http://127.0.0.1:8000/api/sid/organisations/2/" } }


"""
