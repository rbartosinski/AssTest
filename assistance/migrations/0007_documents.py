# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-20 15:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assistance', '0006_newtask_rented_car_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('sms', models.TextField(null=True)),
                ('email', models.TextField(null=True)),
                ('doc_in_file', models.FileField(null=True, upload_to='documents/%Y/%m/%d')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assistance.NewOrder')),
                ('who_add', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
