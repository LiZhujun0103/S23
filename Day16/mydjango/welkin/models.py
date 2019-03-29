from django.db import models

# Create your models here.


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    settime = models.DateField(auto_now=True)


class Appline(models.Model):
    lid = models.AutoField(primary_key=True)
    appname = models.CharField(max_length=64)


class Mainframe(models.Model):
    id = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32)
    paswd = models.CharField(max_length=64)
    line = models.ForeignKey(to='Appline')
