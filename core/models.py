# Django
from django.db import models
# from django.contrib.auth.models import *
# from django.contrib.postgres.fields import ArrayField
# from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import fields
from django.utils import timezone

class Customer(models.Model):
    customerId = models.AutoField(primary_key=True)
    customerName = models.CharField(max_length=512, null=True)
    contactType = models.CharField(max_length=52, null=True)
    contact = models.CharField(max_length=512, null=True)
    isDelete = models.BooleanField(default=False)
    createdDate = models.DateTimeField(editable=False)
    lastModifiedDate = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if not self.customerId:
            self.createdDate = timezone.now()
        else:
            self.lastModifiedDate = timezone.now()
        return super(Customer, self).save(*args, **kwargs)

    class Meta:
        db_table = 'customer'

class Join(models.Model):
    CONTACT_CHOICES = (
        ('whatsapp', 'Whatsapp'),
        ('line', 'Line'),
        ('email', 'Email'),
        ('instagram', 'Instagram')
    )
    joinId = models.AutoField(primary_key=True)
    customerName = models.CharField(max_length=512, null=True)
    contactType = models.CharField(max_length=52, choices=CONTACT_CHOICES)
    contact = models.CharField(max_length=512, null=True)
    pickupPoint = models.CharField(max_length=2056, null=True)
    dropoffPoint = models.CharField(max_length=2056, null=True)
    firstPickupDate = models.DateField(null=True)
    everyTime = models.TimeField(null=True)
    isDelete = models.BooleanField(default=False)
    createdDate = models.DateTimeField(editable=False)
    lastModifiedDate = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if not self.joinId:
            self.createdDate = timezone.now()
        else:
            self.lastModifiedDate = timezone.now()
        return super(Join, self).save(*args, **kwargs)

    class Meta:
        db_table = 'join'

class Later(models.Model):
    CONTACT_CHOICES = (
        ('whatsapp', 'Whatsapp'),
        ('line', 'Line'),
        ('email', 'Email'),
        ('instagram', 'Instagram')
    )
    laterId = models.AutoField(primary_key=True)
    customerName = models.CharField(max_length=512, null=True)
    contactType = models.CharField(max_length=52, choices=CONTACT_CHOICES)
    contact = models.CharField(max_length=512, null=True)
    activityArea = models.CharField(max_length=1024, null=True)
    whyNotNow = models.TextField(null=True)
    suggestion = models.TextField(null=True)
    isDelete = models.BooleanField(default=False)
    createdDate = models.DateTimeField(editable=False)
    lastModifiedDate = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if not self.laterId:
            self.createdDate = timezone.now()
        else:
            self.lastModifiedDate = timezone.now()
        return super(Later, self).save(*args, **kwargs)

    class Meta:
        db_table = 'later'

class Question(models.Model):
    CONTACT_CHOICES = (
        ('email', 'Email'),
        ('whatsapp', 'Whatsapp'),
        ('line', 'Line'),
        ('instagram', 'Instagram')
    )
    questionId = models.AutoField(primary_key=True)
    customerName = models.CharField(max_length=512, null=True)
    contactType = models.CharField(max_length=52, choices=CONTACT_CHOICES)
    contact = models.CharField(max_length=512, null=True)
    question = models.TextField(null=True)
    isDelete = models.BooleanField(default=False)
    createdDate = models.DateTimeField(editable=False)
    lastModifiedDate = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if not self.questionId:
            self.createdDate = timezone.now()
        else:
            self.lastModifiedDate = timezone.now()
        return super(Question, self).save(*args, **kwargs)

    class Meta:
        db_table = 'question'
