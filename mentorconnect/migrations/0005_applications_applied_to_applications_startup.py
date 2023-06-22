# Generated by Django 4.1.6 on 2023-05-17 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0020_rename_applications_mentor_application'),
        ('mentorconnect', '0004_applications'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='applied_to',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.mentor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applications',
            name='startup',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.startup'),
            preserve_default=False,
        ),
    ]