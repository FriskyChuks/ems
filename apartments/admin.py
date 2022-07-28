from django.contrib import admin

from .models import *

admin.site.register(Apartment)
admin.site.register(Occupant)
admin.site.register(ApartmentType)
admin.site.register(Street)
