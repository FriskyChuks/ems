from django.urls import path

from . import views

urlpatterns=[
    path('active_vate_bills/',views.active_vate_bills, name='active_vate_bills'),
    path('send_mail_to_all/',views.send_mail_to_all,name='send_mail_to_all'),
    path('schedule_bills/',views.schedule_bills_view,name='schedule_bills'),
    path('create_monthly_bills/',views.create_monthly_bills,name='create_monthly_bills'),
    path('payment/<bill_id>/',views.payment_view,name='payment'),
    path('pending_bills/',views.pending_bills_view, name='pending_bills'),
    path('pending_bills_detail/<user>/',views.pending_bills_detail_view,name='pending_bills_detail'),
    path('load_wallet/<user_id>/',views.load_wallet_view, name='load_wallet'),
]