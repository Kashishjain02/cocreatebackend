# Generated by Django 4.1.6 on 2023-04-13 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorconnect', '0002_tempmeeting'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='link',
            field=models.TextField(blank=True, null=True),
        ),
    ]
