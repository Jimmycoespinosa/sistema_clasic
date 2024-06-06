from django.db import models

class mdlMain(models.Model):
    Cname = models.CharField(max_length=100)
    Sname = models.CharField(max_length=100)

class setCounty(models.Model):
    Cname = models.CharField(max_length=100)

class setState(models.Model):
    Sname = models.CharField(max_length=100)
    idCountry = models.IntegerField(null=False)

class loadState(models.Model):
    Cname = models.CharField(max_length=100)
    Sname = models.CharField(max_length=100)
    idCountry = models.IntegerField(null=False)
