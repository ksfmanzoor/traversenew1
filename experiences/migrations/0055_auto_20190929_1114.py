# Generated by Django 2.1.5 on 2019-09-29 11:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0054_auto_20190603_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 29, 11, 14, 4, 800643, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 29, 11, 14, 4, 800600, tzinfo=utc), null=True),
        ),
    ]
