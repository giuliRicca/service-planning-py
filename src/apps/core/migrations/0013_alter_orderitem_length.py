# Generated by Django 4.0.1 on 2022-02-09 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_core', '0012_orderitem_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='length',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
