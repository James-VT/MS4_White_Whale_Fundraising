# Generated by Django 3.2.8 on 2022-03-01 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0008_alter_donation_donation_custom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='donation_custom',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='donation',
            name='donation_total',
            field=models.FloatField(default=0),
        ),
    ]
