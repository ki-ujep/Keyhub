# Generated by Django 4.2 on 2023-05-12 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0023_faculty_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='titles',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='titles_after',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
