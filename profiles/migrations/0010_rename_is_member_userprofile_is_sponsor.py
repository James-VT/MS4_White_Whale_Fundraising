# Generated by Django 3.2.8 on 2022-03-14 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_userprofile_is_member'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_member',
            new_name='is_sponsor',
        ),
    ]
