# Generated by Django 4.0.5 on 2022-07-25 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0005_rename_user_occupant_occupant'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='price',
            field=models.DecimalField(decimal_places=2, default='00.00', max_digits=20),
        ),
    ]
