# Generated by Django 4.1.6 on 2023-03-14 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_account_credits'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='startup',
            name='credits',
        ),
        migrations.AddField(
            model_name='mentor',
            name='meetings',
            field=models.JSONField(default=[]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='startup',
            name='meetings',
            field=models.JSONField(default=[]),
            preserve_default=False,
        ),
    ]
