# Generated by Django 2.1.5 on 2019-04-24 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_auto_20190424_1118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='attractions',
            new_name='attraction',
        ),
    ]
