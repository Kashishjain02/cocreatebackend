# Generated by Django 4.1.6 on 2023-03-14 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_remove_startup_credits_mentor_meetings_and_more'),
        ('mentorconnect', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TempMeeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField()),
                ('goals', models.TextField()),
                ('expectations', models.TextField()),
                ('querries', models.TextField()),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('is_completed', models.BooleanField(default=False)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.mentor')),
                ('startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.startup')),
            ],
        ),
    ]
