# Generated by Django 3.0.4 on 2020-04-06 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memoApp', '0002_auto_20200406_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memo',
            name='habbit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='memoApp.Habbit'),
        ),
    ]
