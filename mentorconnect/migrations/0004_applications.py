# Generated by Django 4.1.6 on 2023-05-17 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorconnect', '0003_meeting_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField()),
                ('goals', models.TextField()),
                ('expectations', models.TextField()),
                ('questions', models.TextField()),
                ('is_accepted', models.BooleanField(default=False)),
            ],
        ),
    ]