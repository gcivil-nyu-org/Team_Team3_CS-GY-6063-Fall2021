# Generated by Django 3.2.9 on 2021-11-15 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_event_numberofplayers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='numberOfPlayers',
            field=models.IntegerField(verbose_name='Number of People Needed:'),
        ),
    ]
