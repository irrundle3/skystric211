# Generated by Django 2.2.3 on 2019-09-02 23:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20190813_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 2, 16, 35, 15, 93211), verbose_name='date published'),
        ),
    ]
