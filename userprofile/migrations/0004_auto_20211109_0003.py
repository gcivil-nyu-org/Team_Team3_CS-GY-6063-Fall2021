# Generated by Django 3.2.7 on 2021-11-09 05:03

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20211108_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='distance',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('manhattan', 'MANHATTAN'), ('queens', 'QUEENS'), ('bronx', 'BRONX'), ('brooklyn', 'BROOKLYN'), ('staten_island', 'STATEN ISLAND')], max_length=45, verbose_name='Boroughs Willing to Travel:'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(choices=[('select', 'SELECT'), ('manhattan', 'MANHATTAN'), ('queens', 'QUEENS'), ('bronx', 'BRONX'), ('brooklyn', 'BROOKLYN'), ('staten_island', 'STATEN ISLAND')], default='select', max_length=20, verbose_name='Borough'),
        ),
    ]
