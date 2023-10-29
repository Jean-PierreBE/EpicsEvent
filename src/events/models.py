from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime
# Create your models here.


class Customer(models.Model):

    enterprise_name = models.CharField(max_length=55, verbose_name="Nom de l'entreprise")
    client_name = models.CharField(max_length=55, verbose_name="Responsable client")
    information = models.TextField(max_length=2048, blank=True, verbose_name="Information")
    email = models.EmailField(unique=True, max_length=100, blank=False)
    phone = PhoneNumberField(blank=True)
    author_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                    verbose_name="Contact Commercial")
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.enterprise_name


class Contract(models.Model):
    STATUS = (
        ('SI', 'Signed'),
        ('NS', 'Not signed'),
        ('CA', 'Cancelled'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)
    sign_date = models.DateTimeField()
    amount_contract = models.FloatField(default=0)
    saldo_contract = models.FloatField(default=0)
    status_contract = models.CharField(max_length=55, choices=STATUS, verbose_name="Statut")
    author_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)


class Event(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, default=None)
    begin_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=55, verbose_name="localisation")
    notes = models.TextField(max_length=2048, blank=True, verbose_name="Evènement")
    attendees = models.IntegerField(default=0)
    author_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
