# Generated by Django 3.2.9 on 2021-12-09 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_alter_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
