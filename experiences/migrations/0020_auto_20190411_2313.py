# Generated by Django 2.1.5 on 2019-04-11 23:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0019_auto_20190411_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 4, 11, 23, 13, 13, 961417, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 4, 11, 23, 13, 13, 961388, tzinfo=utc), null=True),
        ),
    ]
