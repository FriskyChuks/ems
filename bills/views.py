# from turtle import delay
from multiprocessing import context
from unicodedata import name
from django.shortcuts import redirect, render, HttpResponse
from django.db.models import Count

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
            "user__email","user","amount_due").annotate(n=models.Count("pk"))
    context={"bills":bills}
    return render(request,'bills/pending_bills.html',context)

def pending_bills_detail_view(request,user):
    occupant = User.objects.get(id=user)
    bills=Bill.objects.filter(status='billed',user=user)
    context={"bills":bills,"occupant":occupant}
    return render(request,'bills/pending_bills_detail.html',context)


def payment_view(request,bill_id):
    bill = Bill.objects.get(id=bill_id)
    payment_obj = Payment.objects.create(amount_paid=bill.amount_due,action='receipt',
                                user_id=bill.user.id,created_by=request.user)
    if payment_obj:
        payment_obj
        obj = PaymentDetail.objects.create(
                bill_id         = bill.id,
                payment_id      = payment_obj.id
            )
        obj.save()
        Bill.objects.filter(id=bill.id).update(status="paid")

    return redirect('pending_bills_detail',user=bill.user.id)

