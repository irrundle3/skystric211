# Generated by Django 2.2.3 on 2019-07-24 19:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20190724_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 24, 12, 39, 17, 825400), verbose_name='date published'),
        ),
    ]
