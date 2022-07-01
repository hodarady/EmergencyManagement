from django.db import models
import datetime
from django.contrib.auth.models import User

class ModelForm1(models.Model):
    name        = models.CharField(max_length = 100)
    age         = models.IntegerField()
    address     = models.CharField(max_length = 100)
    roomNumber  = models.IntegerField()
    date        = models.DateTimeField( ("Date"), default = datetime.datetime.utcnow()+datetime.timedelta(hours=2))
    phonenumber = models.CharField(max_length = 100 )
    gender      = models.CharField(max_length=10 )
    nationalId  = models.CharField(max_length=15 , null = True)
    exitDate    = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class ModelForm2(models.Model):
    forigenKey = models.ForeignKey(ModelForm1 , default = '30' , related_name = 'form2form' , on_delete = models.CASCADE)
    drdep      = models.CharField(max_length = 100)
    department = models.CharField(max_length = 100)
    Diagnosis  = models.CharField(max_length = 100)

    def __str__(self):
        return self.forigenKey.name

class profiles(models.Model):
    user = models.OneToOneField(User , on_delete = models.CASCADE , null = True)
    name        = models.CharField(max_length = 100)
    nationalId  = models.CharField(max_length=15 , null = True)
    age         = models.IntegerField()
    address     = models.CharField(max_length = 100)
    phonenumber = models.CharField(max_length = 100 )
    gender      = models.CharField(max_length=10  , choices = [("MALE" , "MALE") , ("FEMALE" , "FEMAL")])
    email       = models.EmailField()

    def __str__(self):
        return self.name
