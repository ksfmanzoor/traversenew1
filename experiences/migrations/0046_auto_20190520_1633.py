# Generated by Django 2.1.5 on 2019-05-20 16:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0045_auto_20190520_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='gallery',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='itinerary',
        ),
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 20, 16, 33, 7, 72268, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 20, 16, 33, 7, 72235, tzinfo=utc), null=True),
        ),
    ]