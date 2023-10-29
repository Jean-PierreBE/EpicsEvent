from django.contrib import admin
from events.models import Customer, Contract, Event
# Register your models here.

admin.site.register(Customer)

admin.site.register(Contract)

admin.site.register(Event)
