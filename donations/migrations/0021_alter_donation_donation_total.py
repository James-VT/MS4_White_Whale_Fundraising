# Generated by Django 3.2.8 on 2022-03-04 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0020_alter_donation_donation_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='donation_total',
            field=models.CharField(choices=[('£5', '5'), ('£10', '10'), ('£15', '15'), ('£25', '25'), ('£30', '30')], max_length=6),
        ),
    ]
