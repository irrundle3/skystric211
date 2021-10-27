# Generated by Django 2.2.3 on 2019-07-23 21:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190723_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 23, 14, 54, 14, 370373), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cart',
            field=models.ManyToManyField(blank=True, to='main.CartProduct'),
        ),
    ]
