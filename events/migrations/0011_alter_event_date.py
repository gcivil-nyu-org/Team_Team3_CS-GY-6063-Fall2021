# Generated by Django 3.2.7 on 2021-11-25 23:01

from django.db import migrations, models
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_alter_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(validators=[events.models.Event.no_past, events.models.Event.more_than_3hrs], verbose_name='Event Date'),
        ),
    ]