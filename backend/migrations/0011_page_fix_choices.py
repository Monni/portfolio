# Generated by Django 2.0.6 on 2018-07-30 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_pagecontent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='page_name',
            field=models.CharField(choices=[('HOME', 'Home'), ('RESUME', 'Title'), ('PROJECTS', 'Projects')], max_length=10, null=True),
        ),
    ]