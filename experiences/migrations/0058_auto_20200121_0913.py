# Generated by Django 2.1.5 on 2020-01-21 09:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0057_auto_20200121_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 1, 21, 9, 13, 41, 328561, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 1, 21, 9, 13, 41, 328526, tzinfo=utc), null=True),
        ),
    ]
