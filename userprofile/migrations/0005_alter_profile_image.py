# Generated by Django 3.2.9 on 2021-11-22 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_auto_20211109_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='media/profile_pics/default.jpg', upload_to='profile_pics'),
        ),
    ]
