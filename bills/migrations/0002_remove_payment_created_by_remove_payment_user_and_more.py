# Generated by Django 4.0.6 on 2022-08-01 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='paymentdetail',
            name='bill',
        ),
        migrations.RemoveField(
            model_name='paymentdetail',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='paymentdetail',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='resident',
        ),
        migrations.DeleteModel(
            name='Bill',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.DeleteModel(
            name='PaymentDetail',
        ),
        migrations.DeleteModel(
            name='Wallet',
        ),
    ]
