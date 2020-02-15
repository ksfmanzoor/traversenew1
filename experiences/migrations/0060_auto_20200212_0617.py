# Generated by Django 2.1.5 on 2020-02-12 06:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0059_auto_20200121_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='date_booked',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 12, 6, 17, 49, 480263, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='date_booked',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 12, 6, 17, 49, 480263, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 12, 6, 17, 49, 482823, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 12, 6, 17, 49, 482797, tzinfo=utc), null=True),
        ),
    ]