# Generated by Django 2.1.5 on 2019-04-24 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_auto_20190423_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='atrraction',
            name='place',
            field=models.ManyToManyField(blank=True, related_name='places', to='places.Place'),
        ),
        migrations.AlterField(
            model_name='place',
            name='attractions',
            field=models.ManyToManyField(blank=True, related_name='attractions', to='places.Atrraction'),
        ),
    ]
