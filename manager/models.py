from django.db import models

# Create your models here.

class login(models.Model):

    email = models.EmailField(primary_key=True,
                              max_length=255,
                              default='')
    password = models.CharField(max_length=255,
                                default='')

class enquiry(models.Model):
    customer = models.AutoField(primary_key=True)

    name = models.CharField(max_length=225,
                                 default='')

    email = models.EmailField(max_length=225,
                                   default='')

    mobile = models.CharField(max_length=225,
                                   default='')

    destination = models.CharField(max_length=225,
                            default='')

    date = models.CharField(max_length=225,
                            default='')


