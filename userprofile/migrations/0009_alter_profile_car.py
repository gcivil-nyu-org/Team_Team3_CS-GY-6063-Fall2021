# Generated by Django 3.2.7 on 2021-11-09 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0008_alter_profile_distance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='car',
            field=models.CharField(blank=True, choices=[('yes', 'YES'), ('no', 'NO')], max_length=3),
        ),
    ]
