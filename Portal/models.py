from django.db import models
from django.core.validators import MinLengthValidator
from django.utils import timezone


class Link(models.Model):
    linkid = models.AutoField(primary_key=True)
    userrole = models.CharField(max_length=100)
    url = models.CharField(max_length=1000)
    category = models.CharField(max_length=50)
    appname = models.CharField(max_length=50)


class User(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=20)
    password = models.CharField(
        validators=[MinLengthValidator(6)], max_length=20)
    userrole = models.CharField(max_length=100)

    class Meta:
        ordering = ['-userid']

    def __unicode__(self):
        return self.username
