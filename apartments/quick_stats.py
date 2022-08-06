from django.utils import timezone

from bills.models import Payment
from .models import *

def expected_monthly_revenue():
    income = 0.00
    rented_apartments = Apartment.objects.filter(status='taken')
    for apartment in rented_apartments:
        price = apartment.apartment_type.price
        income += float(price)
    return income

def amount_received():
    income = 0.00
    payments = Payment.objects.filter(date_created__gte=timezone.now().replace(
                                day=1, hour=0, minute=0, second=0, microsecond=0))
    for payment in payments:
        income += float(payment.amount_paid)
    return income    