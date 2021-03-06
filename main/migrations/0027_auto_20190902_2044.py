# Generated by Django 2.2.3 on 2019-09-03 03:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20190902_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrontPageImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to='')),
                ('title_text', models.CharField(max_length=300)),
                ('desc_text', models.TextField()),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='productreview',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 2, 20, 44, 58, 921119), verbose_name='date published'),
        ),
    ]
