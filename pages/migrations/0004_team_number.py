# Generated by Django 3.2 on 2021-04-27 19:26

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20210427_0745'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]