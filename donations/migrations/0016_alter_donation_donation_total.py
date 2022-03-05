# Generated by Django 3.2.8 on 2022-03-04 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0015_alter_donation_donation_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='donation_total',
            field=models.CharField(choices=[('5.00', '£5.00'), ('10.00', '£10.00'), ('15.00', '£15.00'), ('25.00', '£25.00'), ('30.00', '£30.00')], max_length=5),
        ),
    ]
