# Generated by Django 2.1.5 on 2019-05-02 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0016_auto_20190502_1222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='type',
        ),
        migrations.AddField(
            model_name='place',
            name='type',
            field=models.ManyToManyField(blank=True, to='places.Type'),
        ),
    ]