# Generated by Django 4.1.6 on 2023-06-22 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0022_waitlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waitlist',
            name='email',
            field=models.EmailField(max_length=100, verbose_name='email'),
        ),
    ]
