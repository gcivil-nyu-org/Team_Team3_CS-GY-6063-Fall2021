# Generated by Django 3.2.7 on 2021-11-09 04:46

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='car',
            field=models.CharField(choices=[('select', 'SELECT'), ('yes', 'YES'), ('no', 'NO')], default='select', max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='distance',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('manhattan', 'MANHATTAN'), ('queens', 'QUEENS'), ('bronx', 'BRONX'), ('brooklyn', 'BROOKLYN'), ('staten_island', 'STATEN ISLAND')], max_length=45),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(choices=[('select', 'SELECT'), ('manhattan', 'MANHATTAN'), ('queens', 'QUEENS'), ('bronx', 'BRONX'), ('brooklyn', 'BROOKLYN'), ('staten_island', 'STATEN ISLAND')], default='select', max_length=20),
        ),
    ]
