# Generated by Django 2.1.5 on 2020-01-21 09:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0056_auto_20200121_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 1, 21, 9, 12, 2, 974921, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 1, 21, 9, 12, 2, 974886, tzinfo=utc), null=True),
        ),
    ]
