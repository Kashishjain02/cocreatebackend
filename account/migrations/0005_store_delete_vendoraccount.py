# Generated by Django 4.1.6 on 2023-02-06 12:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_vendoraccount_shop_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('vendor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('email', models.EmailField(max_length=100, verbose_name='email')),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('plan', models.CharField(choices=[('starter', 'Starter'), ('economic', 'Economic')], default='starter', max_length=20)),
                ('template', models.CharField(default='default,default', max_length=20)),
                ('subscripton_amount', models.IntegerField(blank=True, null=True)),
                ('shop_name', models.CharField(max_length=150, unique=True)),
                ('shop_add', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=20)),
                ('gst', models.CharField(blank=True, max_length=30, null=True)),
                ('subscription_active', models.BooleanField(default=False)),
                ('is_blocked', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='VendorAccount',
        ),
    ]
