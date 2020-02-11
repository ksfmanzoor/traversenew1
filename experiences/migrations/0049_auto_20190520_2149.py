# Generated by Django 2.1.5 on 2019-05-20 21:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0048_auto_20190520_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='experiences',
            field=models.ManyToManyField(blank=True, to='experiences.Experience'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 20, 21, 49, 10, 903950, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 20, 21, 49, 10, 903913, tzinfo=utc), null=True),
        ),
    ]
