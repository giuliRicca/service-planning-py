# Generated by Django 4.0.1 on 2022-02-02 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_core', '0004_rename_servicetimes_servicetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicetype',
            name='teams',
            field=models.ManyToManyField(blank=True, to='apps_core.Team'),
        ),
    ]
