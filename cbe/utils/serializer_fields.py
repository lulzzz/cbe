from urllib.parse import urlparse
from django.core.urlresolvers import resolve
from django.utils import six
from rest_framework import serializers

from cbe.party.models import Individual, Organisation, TelephoneNumber
#from cbe.party.serializers import IndividualSerializer, OrganisationSerializer


class GenericRelatedField(serializers.StringRelatedField):

    """
    A custom field to use for serializing generic relationships.
    """

    def __init__(self, serializer_dict, *args, **kwargs):
        super(GenericRelatedField, self).__init__(*args, **kwargs)

        self.serializer_dict = serializer_dict
        for s in self.serializer_dict.values():
            s.bind('', self)


    def to_representation(self, instance):
        # find a serializer correspoding to the instance class
        for key in self.serializer_dict.keys():
            if isinstance(instance, key):
                # Return the result of the classes serializer
                return self.serializer_dict[key].to_representation(instance=instance)
        return '{}'.format(instance)


    def to_internal_value(self, data):
        # If provided as string, must be url to resource. Create dict
        # containing just url
        if type(data) == str:
            data = {'url': data}

        print(data)
        print(data)
        print(data)

        # Existing resource can be specified as url
        if 'url' in data:
            # Extract details from the url and grab real object
            resolved_func, unused_args, resolved_kwargs = resolve(
                urlparse(data['url']).path)
            object = resolved_func.cls.queryset.get(pk=resolved_kwargs['pk'])
            print(object)
            print(object)
            print(object)
        else:
            # If url is not specified then object is new and must have a 'type'
            # field to allow us to create correct object from list of
            # serializers
            for key in self.serializer_dict.keys():
                if data['type'] == key.__name__:
                    object = key()

        # Deserialize data into attributes of object and apply
        if object.__class__ in self.serializer_dict.keys():
            serializer = self.serializer_dict[object.__class__]
            print(serializer.__dict__)
            print(serializer.__dict__)
            print(serializer.__dict__)
            serializer.partial = True
            obj_internal_value = serializer.to_internal_value(data)
            for k, v in obj_internal_value.items():
                setattr(object, k, v)
        else:
            raise NameError(
                "No serializer specified for {} entities".format(object.__class__.__name__))

        # Save object to store new or any updated attributes
        object.save()
        return object


class TypeField(serializers.Field):

    """
        Read only Field which displays the object type from the class name
    """

    def __init__(self, *args, **kwargs):

        kwargs['source'] = '__class__.__name__'
        kwargs['read_only'] = True
        super(TypeField, self).__init__(*args, **kwargs)

    def to_representation(self, value):
        return value
