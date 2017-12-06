from django.db import models

# Create your models here.
class Program(models.Model):
    name=models.CharField( max_length=100 )
    def __unicode__(self):
        return self.name   
    @classmethod
    def create(cls, name):
        program = cls(name=name)
        # do something with the book
        return program 
    
class Bundle(models.Model):
    name=models.CharField( max_length=100 )
    programId=models.IntegerField(default=0)
    def __unicode__(self):
        return self.name      
    
class Firmware(models.Model):
    version=models.CharField( max_length=100 ) # ROM01
    category=models.CharField( max_length=10 ) # FC/RC/MR
    bundleId=models.IntegerField(default=0)
    def __unicode__(self):
        return self.version       

class Software(models.Model):
    version=models.CharField( max_length=100 ) # 46.0.0.001
    category=models.CharField( max_length=10 ) # FC/RC/MR
    bundleId=models.IntegerField(default=0)
    def __unicode__(self):
        return self.version
    
class Report(models.Model):
    name=models.CharField( max_length=100 )
    programId=models.IntegerField(default=0)
    bundleId=models.IntegerField(default=0)
    firmwareId=models.IntegerField(default=0)
    softwareId=models.IntegerField(default=0)
    path=models.CharField( max_length=100, default='' )
    def __unicode__(self):
        return self.name        
    
