# from turtle import delay
from unicodedata import name
from django.shortcuts import redirect, render, HttpResponse
from .task import create_bills_for_all

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
        hour=20,minute=45
    )
    task = PeriodicTask.objects.create(crontab=schedule, 
    name='Schedule Bills Creation_9', 
    task='bills.task.create_bills_for_all')

    return redirect('schedule_bills')
