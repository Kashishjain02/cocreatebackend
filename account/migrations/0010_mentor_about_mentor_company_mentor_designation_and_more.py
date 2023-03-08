# Generated by Django 4.1.6 on 2023-02-18 10:11

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_mentor_rename_subscripton_amount_startup_credits_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='about',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mentor',
            name='company',
            field=models.CharField(default='google', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mentor',
            name='designation',
            field=models.CharField(default='ceo', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mentor',
            name='name',
            field=models.CharField(default='ram', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='startup',
            name='about',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
