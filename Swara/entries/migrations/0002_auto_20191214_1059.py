# Generated by Django 3.0 on 2019-12-14 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='body',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='slug',
        ),
        migrations.AddField(
            model_name='entry',
            name='upload',
            field=models.FileField(default='default.mp3', upload_to='media/'),
        ),
    ]
