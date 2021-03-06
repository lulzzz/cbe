from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from gm2m import GM2MField

from cbe.location.models import Country

GENDER_CHOICES = (('Undisclosed', 'Undisclosed'),
                  ('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'))
MARITAL_STATUS_CHOICES = (('Undisclosed', 'Undisclosed'),
                          ('Single', 'Single'), ('Married', 'Married'), ('Other', 'Other'))


class Party(models.Model):
    name = models.CharField(max_length=200)
    party_user = models.ForeignKey(User, blank=True, null=True)

    class Meta:
        abstract = True


class Individual(Party):
    gender = models.CharField(
        max_length=50, blank=True, null=True, choices=GENDER_CHOICES)
    family_names = models.CharField(max_length=200, blank=True)
    given_names = models.CharField(max_length=200, blank=True)
    middle_names = models.CharField(max_length=200, blank=True)
    form_of_address = models.CharField(max_length=100, blank=True)
    legal_name = models.CharField(max_length=200, blank=True)
    marital_status = models.CharField(
        max_length=100, null=True, blank=True, choices=MARITAL_STATUS_CHOICES)
    nationality = models.ForeignKey(Country, blank=True, null=True)
    place_of_birth = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        form = ""
        if self.form_of_address != "":
            form = self.form_of_address + " "
        if self.middle_names != "":
            self.name = form + \
                " ".join(
                    [self.given_names, self.middle_names, self.family_names])
        elif self.given_names != "":
            self.name = form + " ".join([self.given_names, self.family_names])

        super(Individual, self).save(*args, **kwargs)


class Organisation(Party):  # Eg IRD
    organisation_type = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class PartyRole(models.Model):
    valid_from = models.DateTimeField(auto_now_add=True)
    valid_to = models.DateTimeField(null=True, blank=True)

    name = models.CharField(max_length=200)
    party_content_type = models.ForeignKey(
        ContentType, related_name="%(app_label)s_%(class)s_ownership")
    party_object_id = models.PositiveIntegerField()
    party = GenericForeignKey('party_content_type', 'party_object_id')

    contact_mediums = GM2MField()

    class Meta:
        abstract = True

    @property
    def individual(self):
        if type(self.party) is Individual:
            return self.party

    @individual.setter
    def individual(self, value):
        if type(value) is Individual or value == None:
            self.party = value
        else:
            raise Exception(
                "Invalid type of party provided as individual to PartyRole: %s" % type(value))

    @property
    def organisation(self):
        if type(self.party) is Organisation:
            return self.party

    @organisation.setter
    def organisation(self, value):
        if type(value) is Organisation or value == None:
            self.party = value
        else:
            raise Exception(
                "Invalid type of party provided as organisation to PartyRole: %s" % type(value))

    def __str__(self):
        return "%s as a %s" % (self.party, self.name)


class GenericPartyRole(PartyRole):
    pass

    
class Owner(PartyRole):

    def save(self, *args, **kwargs):
        if self.name == "":
            self.name = "Owner"          
        super(Owner, self).save(*args, **kwargs)

        
class ContactMedium(models.Model):
    # TODO: Restrict to PartyRole derrived types
    valid_from = models.DateField(null=True, blank=True)
    valid_to = models.DateField(null=True, blank=True)

    party_role_content_type = models.ForeignKey(
        ContentType, related_name="%(class)s", null=True)
    party_role_object_id = models.PositiveIntegerField(null=True)
    party_role = GenericForeignKey(
        'party_role_content_type', 'party_role_object_id')

    class Meta:
        abstract = True


class TelephoneNumber(ContactMedium):
    number = models.CharField(max_length=50)

    def __str__(self):
        return self.number


class EmailContact(ContactMedium):
    email_address = models.EmailField(max_length=200)  # , unique=True)

    def __str__(self):
        return self.email_address


class PhysicalContact(ContactMedium):
    # TODO: Restrict to Address derrived types
    address_content_type = models.ForeignKey(
        ContentType, related_name="%(app_label)s_%(class)s_address_ownership")
    address_object_id = models.PositiveIntegerField()
    address = GenericForeignKey('address_content_type', 'address_object_id')
