# Generated by Django 3.2.8 on 2022-03-04 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0013_alter_donation_donation_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='donation_total',
            field=models.CharField(choices=[('5.00', '£5'), ('10.00', '£10'), ('15.00', '£15'), ('25.00', '£25'), ('30.00', '£30')], max_length=5),
        ),
    ]