# Generated by Django 4.0.1 on 2022-02-02 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps_core', '0003_servicetimes_teams_servicetypes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ServiceTimes',
            new_name='ServiceTime',
        ),
        migrations.RenameModel(
            old_name='ServiceTypes',
            new_name='ServiceType',
        ),
        migrations.RenameModel(
            old_name='Teams',
            new_name='Team',
        ),
    ]
