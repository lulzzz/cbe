from django.db import models

from cbe.party.models import Organisation

class PhysicalObject(models.Model):
    start_date = models.DateTimeField(null=True,blank=True)
    end_date = models.DateTimeField(null=True,blank=True)
    physical_object_type = models.CharField(max_length=100)
    #place

    class Meta:
        abstract = True

        
class ManufacturedObject(PhysicalObject):
    make = models.ForeignKey(Organisation)

    class Meta:
        abstract = True
        
        
class Structure(ManufacturedObject):

    def __str__(self):
        return self.physical_object_type

    def save(self, *args, **kwargs):
        if self.physical_object_type is None or self.physical_object_type == "":
            self.physical_object_type = "Structure"          
        super(Structure, self).save(*args, **kwargs)
        
        
class Vehicle(ManufacturedObject):
    series = models.CharField(max_length=100)
    model = models.CharField(max_length=100,blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    
    engine_capacity = models.IntegerField(blank=True, null=True)
    engine_type = models.CharField(max_length=100, blank=True, null=True)
    
    body_style = models.CharField(max_length=100, blank=True, null=True)
    doors = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    axles = models.IntegerField(blank=True, null=True)
    
    
    def __str__(self):
        if self.model is not None:
            return "%s %s %s" %(self.make, self.series, self.model)
        return "%s %s" %(self.make, self.series)

        
    def save(self, *args, **kwargs):
        if self.physical_object_type is None or self.physical_object_type == "":
            self.physical_object_type = "Vehicle"          
        super(Vehicle, self).save(*args, **kwargs)
         