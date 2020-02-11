# Generated by Django 2.1.5 on 2019-04-11 23:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0014_auto_20190411_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 4, 11, 23, 6, 0, 841253, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 4, 11, 23, 6, 0, 841221, tzinfo=utc), null=True),
        ),
    ]
