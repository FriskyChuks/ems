from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Bill)
admin.site.register(Payment)
admin.site.register(PaymentDetail)
admin.site.register(Wallet)