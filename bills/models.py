from django.conf import settings
from django.db import models

from accounts.models import *
from apartments.models import *

BILL_STATUS = (
        ("billed","Billed"),
        ("paid","Paid")
    )

PAY_ACTION = (
        ("deposit","Deposit"),
        ("receipt","Receipt"),
    )


class Bill(models.Model):
    occupant                = models.ForeignKey(User, on_delete=models.CASCADE)
    billed_for          = models.ForeignKey(Apartment,on_delete=models.CASCADE)
    amount_due          = models.DecimalField(decimal_places=2, default='00.00', max_digits=20)
    status              = models.CharField(max_length=10, choices=BILL_STATUS, default='billed')
    date_created        = models.DateField(auto_now_add=False, auto_now=True)
    last_updated        = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return f"{self.billed_for}({self.amount_due}) || {self.user.email}"


class Payment(models.Model):
    amount_paid     = models.DecimalField(decimal_places=2, default='00.00', max_digits=20)
    action          = models.CharField(max_length=20, choices=PAY_ACTION)
    occupant        = models.ForeignKey(User, on_delete=models.CASCADE)
    created_by      = models.ForeignKey(User,related_name='created_by',on_delete=models.CASCADE, null=True, blank=True)
    date_created    = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return str(self.amount_paid)


class PaymentDetail(models.Model):
    bill            = models.ForeignKey(Bill, on_delete=models.CASCADE, blank=True, null=True)
    payment         = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True, blank=True)
    date_created    = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"{self.bill.billed_for} {self.bill.amount_due}"
        

class Wallet(models.Model):
    occupant        = models.OneToOneField(User,related_name='resident', on_delete=models.CASCADE, null=True, blank=True)
    account_balance = models.DecimalField(decimal_places=2, default='00.00', max_digits=20)
    created_by      = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_created    = models.DateTimeField(auto_now_add=False, auto_now=True)
    last_updated    = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return f"N{self.account_balance} || {self.occupant.email}"



