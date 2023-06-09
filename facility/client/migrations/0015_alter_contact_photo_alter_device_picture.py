# Generated by Django 4.2 on 2023-04-22 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0014_remove_device_picture_path_device_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='photo',
            field=models.ImageField(blank=True, default='managers/male.png', upload_to='managers'),
        ),
        migrations.AlterField(
            model_name='device',
            name='picture',
            field=models.ImageField(null=True, upload_to='device_pictures/'),
        ),
    ]
