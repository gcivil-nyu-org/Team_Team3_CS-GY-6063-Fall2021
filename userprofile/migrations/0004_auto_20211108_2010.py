# Generated by Django 3.2.7 on 2021-11-09 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_alter_profile_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borough',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('travel', models.CharField(choices=[('select', 'SELECT'), ('manhattan', 'MANHATTAN'), ('queens', 'QUEENS'), ('bronx', 'BRONX'), ('brooklyn', 'BROOKLYN'), ('staten_island', 'STATEN ISLAND')], default='select', max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='distance',
        ),
        migrations.AddField(
            model_name='profile',
            name='distance',
            field=models.ManyToManyField(to='userprofile.Borough'),
        ),
    ]
