# Generated by Django 3.2.8 on 2022-03-04 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0021_alter_donation_donation_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='donation_total',
            field=models.CharField(max_length=6),
        ),
    ]
