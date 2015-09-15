# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0003_topping'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('order_time', models.DateTimeField(auto_created=True)),
                ('status', models.CharField(default='pending', choices=[('accepted', 'accepted'), ('declined', 'declined'), ('pending', 'pending'), ('completed', 'completed')], max_length=16)),
                ('order_update', models.DateTimeField(auto_now=True)),
                ('accept_time', models.DateTimeField(null=True, blank=True)),
                ('completed_time', models.DateTimeField(null=True, blank=True)),
                ('shop', models.ForeignKey(to='shop.Shop')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
