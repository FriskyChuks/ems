from django.contrib import messages
from multiprocessing import context
from unicodedata import name
from django.shortcuts import redirect, render, HttpResponse
from django.db.models import Count
from django.contrib.auth.decorators import login_required

from .task import create_bills_for_all
from apartments.models import *
from .models import *

from django_celery_beat.models import PeriodicTask, CrontabSchedule
from mails.task import send_mail_func

def active_vate_bills(request):
    create_bills_for_all.delay()
    return HttpResponse('Done Testing')


def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse('Mail sent successfully!')


def schedule_bills_view(request):
    schedule, created = CrontabSchedule.objects.get_or_create(
        hour=13,minute=4
    )
    task = PeriodicTask.objects.create(crontab=schedule, 
    name='Schedule Bills Creation_4', 
    task='bills.task.create_bills_for_all')

    return redirect('schedule_bills')


def create_monthly_bills(request):
    occupant=Occupant.objects.all()
    apartments=Apartment.objects.filter(status='taken')
    for apartment in apartments:
        for c in apartment.occupant_set.all():
            bill_obj=Bill.objects.create(user_id=c.occupant.id,status='billed',
                        billed_for_id=apartment.id,amount_due=10.00,      
                    )
            bill_obj.save()
    return redirect('pending_bills')

def pending_bills_view(request):
    bills=Bill.objects.filter(status='billed').order_by().values(
            "occupant__email","occupant","amount_due").annotate(n=models.Count("pk"))
    context={"bills":bills}
    return render(request,'bills/pending_bills.html',context)

def pending_bills_detail_view(request,user):
    occupant = User.objects.get(id=user)
    bills=Bill.objects.filter(status='billed',occupant=user)
    account_balance = Wallet.objects.get(occupant_id=user).account_balance
    context={"bills":bills,"occupant":occupant,"account_balance":account_balance}
    return render(request,'bills/pending_bills_detail.html',context)


@login_required(login_url="login")
def payment_view(request,bill_id):
    bill = Bill.objects.get(id=bill_id)
    account_balance = Wallet.objects.get(occupant_id=bill.occupant.id).account_balance
    if (float(account_balance) <= float(bill.amount_due)):
        messages.error(request, "Account balance is too low, please top-up!")
        return redirect('pending_bills_detail',user=bill.occupant.id)
    else:
        payment_obj = Payment.objects.create(amount_paid=bill.amount_due,action='receipt',
                                occupant_id=bill.occupant.id,created_by=request.user)
        # if payment_obj:
        account_balance = float(account_balance) - float(bill.amount_due)
        Wallet.objects.filter(occupant_id=bill.occupant.id).update(account_balance=account_balance)
        PaymentDetail.objects.create(bill_id= bill.id,payment_id= payment_obj.id)
        Bill.objects.filter(id=bill.id).update(status="paid")
        messages.success(request, "Payment updated successfully!")

    return redirect('pending_bills_detail',user=bill.occupant.id)


@login_required(login_url="login")
def load_wallet_view(request,user_id):
    user=User.objects.get(id=user_id)
    account_balance = Wallet.objects.get(occupant_id=user_id).account_balance
    deposit_amount = request.POST.get('amount')
    if request.method=='POST':   
        new_balance = float(account_balance) + float(deposit_amount)
        Wallet.objects.filter(occupant_id=user_id).update(account_balance=new_balance)
        Payment.objects.create(amount_paid=deposit_amount,
                action='deposit',occupant_id=user_id,created_by_id=request.user.id
        )
        messages.success(request, "Wallet loaded successfully!")
        return redirect("load_wallet",user_id)
    context={"user":user,"account_balance":account_balance}
    return render(request,'bills/load_wallet.html',context)