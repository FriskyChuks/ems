from django.utils import timezone

from bills.models import Bill, Payment
from .models import *

def expected_monthly_revenue():
    income = 0.00
    bills = Bill.objects.filter(date_created__gte=timezone.now().replace(
                                day=1, hour=0, minute=0, second=0, microsecond=0))
    for bill in bills:
        price = bill.amount_due
        income += float(price)
    return income

def amount_received():
    income = 0.00
    payments = Payment.objects.filter(date_created__gte=timezone.now().replace(
                                day=1, hour=0, minute=0, second=0, microsecond=0))
    for payment in payments:
        income += float(payment.amount_paid)
    return income    