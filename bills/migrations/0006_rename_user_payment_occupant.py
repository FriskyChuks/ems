# Generated by Django 4.0.6 on 2022-08-02 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0005_rename_resident_wallet_occupant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='user',
            new_name='occupant',
        ),
    ]
