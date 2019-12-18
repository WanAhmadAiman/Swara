# Generated by Django 3.0 on 2019-12-17 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0002_auto_20191218_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='word',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='record.Word'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='title',
            field=models.CharField(max_length=10),
        ),
    ]
