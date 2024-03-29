# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-03 13:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admins', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodqty', models.IntegerField()),
                ('location', models.CharField(max_length=200)),
                ('dateordered', models.DateField(auto_now=True)),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.Products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratings', models.IntegerField(max_length=200)),
                ('reviews', models.CharField(max_length=200)),
                ('orders', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Orders')),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.Products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
