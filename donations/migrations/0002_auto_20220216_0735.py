# Generated by Django 3.2.8 on 2022-02-16 07:35

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donation',
            old_name='full_name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='donation',
            name='last_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='donation',
            name='title',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='donation',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
