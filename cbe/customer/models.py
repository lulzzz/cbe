from functools import partial

from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_init, post_save

from cbe.party.models import GenericPartyRole, PartyRole
from cbe.business_interaction.models import BusinessInteraction, BusinessInteractionItem

customer_status_choices = (('new', 'new'), ('active', 'active'),
                           ('inactive', 'inactive'), ('prospective', 'prospective'))


class Customer(PartyRole):
    customer_number = models.CharField(primary_key=True, max_length=200)
    customer_status = models.CharField(max_length=100, choices=customer_status_choices)

    def save(self, *args, **kwargs):
        self.name = "Customer"
        super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return "%s:%s" % (self.customer_number, self.party)


class CustomerAccountContact(PartyRole):

    def save(self, *args, **kwargs):
        self.name = "CustomerAccountContact"
        super(CustomerAccountContact, self).save(*args, **kwargs)


class CustomerAccount(models.Model):
    account_number = models.CharField(primary_key=True, max_length=200)
    customer = models.ForeignKey(Customer)
    account_status = models.CharField(max_length=100)
    account_type = models.CharField(max_length=200)
    name = models.CharField(max_length=300)
    pin = models.CharField(max_length=100, null=True, blank=True)
    credit_limit = models.CharField(max_length=100, null=True, blank=True)
    customer_account_contact = models.ManyToManyField(CustomerAccountContact, blank=True)

    def __str__(self):
        return "%s:%s" % (self.account_number, self.name)


class CustomerAccountRelationship(models.Model):
    valid_from = models.DateField(null=True, blank=True)
    valid_to = models.DateField(null=True, blank=True)
    relationship_type = models.CharField(max_length=200)
    from_account = models.ForeignKey( CustomerAccount, related_name='related_from_account')
    to_account = models.ForeignKey( CustomerAccount, related_name='related_to_account')


class CustomerOrder(BusinessInteraction):
    customer_order_type = models.CharField(max_length=200, null=True, blank=True)


class CustomerOrderItem(BusinessInteractionItem):
	pass

