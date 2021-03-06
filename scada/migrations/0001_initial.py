# Generated by Django 2.0.5 on 2018-05-19 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rotationspeed', models.IntegerField(choices=[(1, 'LOW'), (2, 'MEDIUM'), (3, 'HIGH')], default=1)),
                ('lightsensor', models.FloatField(default=0.0)),
                ('temperature', models.FloatField(default=0.0)),
                ('soilmoisture', models.FloatField(default=0.0)),
            ],
        ),
    ]
