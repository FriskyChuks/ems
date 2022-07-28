from django.urls import path

from . import views

urlpatterns=[
    path('active_vate_bills/',views.active_vate_bills, name='active_vate_bills'),
    path('send_mail_to_all/',views.send_mail_to_all,name='send_mail_to_all'),
    path('schedule_bills/',views.schedule_bills_view,name='schedule_bills')
]