from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from cbe.party.models import Individual, Organisation, TelephoneNumber, GenericPartyRole, Owner
from cbe.party.serializers import IndividualSerializer, OrganisationSerializer, TelephoneNumberSerializer, GenericPartyRoleSerializer, OwnerSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly, )
    
    
class IndividualViewSet(viewsets.ModelViewSet):
    queryset = Individual.objects.all()
    serializer_class = IndividualSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    #                      IsOwnerOrReadOnly,)

    # def perform_create(self, serializer):
    #    serializer.save(owner=self.request.user)


class OrganisationViewSet(viewsets.ModelViewSet):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class TelephoneNumberViewSet(viewsets.ModelViewSet):
    queryset = TelephoneNumber.objects.all()
    serializer_class = TelephoneNumberSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class GenericPartyRoleViewSet(viewsets.ModelViewSet):
    queryset = GenericPartyRole.objects.all()
    serializer_class = GenericPartyRoleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
