# Generated by Django 4.0.1 on 2022-02-11 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_core', '0013_alter_orderitem_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='item_type',
            field=models.CharField(choices=[('a', 'Item'), ('b', 'Header')], default='a', max_length=1, null=True),
        ),
    ]
