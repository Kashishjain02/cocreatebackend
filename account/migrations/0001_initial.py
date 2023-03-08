# Generated by Django 4.1.5 on 2023-01-24 10:07

import account.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=100, unique=True, verbose_name="email"
                    ),
                ),
                ("viewpass", models.CharField(blank=True, max_length=30, null=True)),
                ("name", models.CharField(max_length=100)),
                (
                    "contact_number",
                    models.IntegerField(blank=True, default=0, null=True),
                ),
                ("is_superuser", models.BooleanField(default=False)),
                ("is_admin", models.BooleanField(default=False)),
                ("is_Vendor", models.BooleanField(default=False)),
                ("is_Blogger", models.BooleanField(default=False)),
                ("is_Affiliate", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="BloggerAccount",
            fields=[
                (
                    "blogger",
                    models.OneToOneField(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("email", models.EmailField(max_length=100, verbose_name="email")),
                ("plan", models.CharField(default="no active plan", max_length=20)),
                ("subscripton_amount", models.IntegerField(blank=True, null=True)),
                ("blogname", models.CharField(max_length=30, unique=True)),
                ("bio", models.CharField(blank=True, max_length=150, null=True)),
                ("address", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=30)),
                ("state", models.CharField(max_length=20)),
                (
                    "template",
                    models.CharField(default="default,default", max_length=20),
                ),
                (
                    "logo",
                    models.ImageField(
                        default="/default-img/titlelogo.png",
                        upload_to=account.models.get_uplaod_file_name_blog,
                    ),
                ),
                (
                    "corousel1",
                    models.ImageField(
                        default="/default-img/main-slider1.jpg",
                        upload_to=account.models.get_uplaod_file_name_blog,
                    ),
                ),
                (
                    "corousel2",
                    models.ImageField(
                        default="/default-img/main-slider2.jpg",
                        upload_to=account.models.get_uplaod_file_name_blog,
                    ),
                ),
                (
                    "corousel3",
                    models.ImageField(
                        default="/default-img/main-slider3.jpg",
                        upload_to=account.models.get_uplaod_file_name_blog,
                    ),
                ),
                (
                    "corousel4",
                    models.ImageField(
                        default="/default-img/slider1.jpg",
                        upload_to=account.models.get_uplaod_file_name_blog,
                    ),
                ),
                (
                    "corousel5",
                    models.ImageField(
                        default="/default-img/main-slider1.jpg",
                        upload_to=account.models.get_uplaod_file_name_blog,
                    ),
                ),
                (
                    "corousel6",
                    models.ImageField(
                        default="/default-img/slider1.jpg",
                        upload_to=account.models.get_uplaod_file_name_blog,
                    ),
                ),
                (
                    "corousel7",
                    models.ImageField(
                        default="/default-img/slider2.jpg",
                        upload_to=account.models.get_uplaod_file_name_blog,
                    ),
                ),
                (
                    "corousel8",
                    models.ImageField(
                        default="/default-img/slider4.jpg",
                        upload_to=account.models.get_uplaod_file_name_blog,
                    ),
                ),
                ("subscription_active", models.BooleanField(default=False)),
                ("is_blocked", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="VendorAccount",
            fields=[
                (
                    "vendor",
                    models.OneToOneField(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("email", models.EmailField(max_length=100, verbose_name="email")),
                ("shop_number", models.IntegerField(blank=True, null=True)),
                ("plan", models.CharField(default="no active plan", max_length=20)),
                (
                    "template",
                    models.CharField(default="default,default", max_length=20),
                ),
                ("subscripton_amount", models.IntegerField(blank=True, null=True)),
                ("shop_name", models.CharField(max_length=150, unique=True)),
                ("shop_add", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=30)),
                ("state", models.CharField(max_length=20)),
                ("gst", models.CharField(blank=True, max_length=30, null=True)),
                (
                    "logo",
                    models.ImageField(
                        default="/default-img/titlelogo.png",
                        upload_to=account.models.get_uplaod_file_name,
                    ),
                ),
                (
                    "corousel1",
                    models.ImageField(
                        default="/default-img/main-slider1.jpg",
                        upload_to=account.models.get_uplaod_file_name,
                    ),
                ),
                (
                    "corousel2",
                    models.ImageField(
                        default="/default-img/main-slider2.jpg",
                        upload_to=account.models.get_uplaod_file_name,
                    ),
                ),
                (
                    "corousel3",
                    models.ImageField(
                        default="/default-img/main-slider3.jpg",
                        upload_to=account.models.get_uplaod_file_name,
                    ),
                ),
                (
                    "corousel4",
                    models.ImageField(
                        default="/default-img/slider1.jpg",
                        upload_to=account.models.get_uplaod_file_name,
                    ),
                ),
                (
                    "corousel5",
                    models.ImageField(
                        default="/default-img/main-slider1.jpg",
                        upload_to=account.models.get_uplaod_file_name,
                    ),
                ),
                (
                    "corousel6",
                    models.ImageField(
                        default="/default-img/slider1.jpg",
                        upload_to=account.models.get_uplaod_file_name,
                    ),
                ),
                (
                    "corousel7",
                    models.ImageField(
                        default="/default-img/slider2.jpg",
                        upload_to=account.models.get_uplaod_file_name,
                    ),
                ),
                (
                    "corousel8",
                    models.ImageField(
                        default="/default-img/slider4.jpg",
                        upload_to=account.models.get_uplaod_file_name,
                    ),
                ),
                ("subscription_active", models.BooleanField(default=False)),
                ("is_blocked", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
    ]