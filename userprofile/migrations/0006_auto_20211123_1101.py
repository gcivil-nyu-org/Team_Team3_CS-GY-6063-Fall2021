# Generated by Django 3.2.7 on 2021-11-23 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_alter_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='adultBaseball',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='adultFootball',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='adultSoftball',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='littleLeagueBaseball',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='littleLeagueSoftball',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='tBall',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='youthFootball',
        ),
    ]
