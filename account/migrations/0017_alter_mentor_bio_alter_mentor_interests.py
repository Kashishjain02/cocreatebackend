# Generated by Django 4.1.6 on 2023-03-15 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_rename_city_startup_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='interests',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
