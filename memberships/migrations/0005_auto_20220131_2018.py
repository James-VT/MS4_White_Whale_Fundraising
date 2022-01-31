# Generated by Django 3.2.8 on 2022-01-31 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0004_remove_membership_sku'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='name',
        ),
        migrations.AddField(
            model_name='membership',
            name='membership_level',
            field=models.CharField(choices=[('Gold', 'Gold Level'), ('Silver', 'Silver Level'), ('Bronze', 'Bronze Level')], default='Bronze', max_length=6),
        ),
    ]