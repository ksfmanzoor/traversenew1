# Generated by Django 2.1.5 on 2019-04-24 20:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0028_auto_20190424_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 4, 24, 20, 5, 38, 22855, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 4, 24, 20, 5, 38, 22825, tzinfo=utc), null=True),
        ),
    ]
