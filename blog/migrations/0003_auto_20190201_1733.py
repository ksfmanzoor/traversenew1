# Generated by Django 2.1.5 on 2019-02-01 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(default='defualt.jpg', upload_to='blog_images'),
        ),
    ]
