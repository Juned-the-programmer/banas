# Generated by Django 3.0.4 on 2020-04-15 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0003_dailyentry'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bill',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='DailyEntry',
        ),
    ]
