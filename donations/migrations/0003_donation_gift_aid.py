# Generated by Django 3.2.8 on 2022-02-16 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0002_auto_20220216_0735'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='gift_aid',
            field=models.BooleanField(default=False),
        ),
    ]