# Generated by Django 4.1.6 on 2023-03-15 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_alter_startup_address_alter_startup_city_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='startup',
            old_name='city',
            new_name='country',
        ),
    ]
