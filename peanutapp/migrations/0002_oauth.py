# Generated by Django 2.2.6 on 2019-12-18 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peanutapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='oauth',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nickname', models.CharField(max_length=50)),
                ('reg_date', models.DateField()),
            ],
        ),
    ]
