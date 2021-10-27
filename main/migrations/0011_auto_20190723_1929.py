# Generated by Django 2.2.3 on 2019-07-24 02:29

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20190723_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 23, 19, 29, 13, 167863), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
