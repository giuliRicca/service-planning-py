# Generated by Django 4.0.1 on 2022-02-09 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_core', '0009_eventorder_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='person',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]