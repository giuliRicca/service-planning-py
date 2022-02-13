# Generated by Django 4.0.1 on 2022-02-02 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_core', '0002_alter_event_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceTimes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155, unique=True)),
                ('recur', models.CharField(choices=[('a', 'Weekly'), ('b', 'Daily'), ('c', 'Every Weekday'), ('e', 'Every Other Week'), ('d', 'Monthly')], default='a', max_length=1, null=True)),
                ('teams', models.ManyToManyField(to='apps_core.Teams')),
                ('times', models.ManyToManyField(to='apps_core.ServiceTimes')),
            ],
        ),
    ]