# Generated by Django 2.2.5 on 2020-11-11 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_auto_20201111_1938'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='amenity',
            options={'verbose_name_plural': 'Amenities'},
        ),
        migrations.AlterModelOptions(
            name='facility',
            options={'verbose_name_plural': 'Facilities'},
        ),
        migrations.AlterModelOptions(
            name='houserule',
            options={'verbose_name_plural': 'House rule'},
        ),
        migrations.AlterModelOptions(
            name='roomtype',
            options={'ordering': ['name'], 'verbose_name_plural': 'Room Type'},
        ),
        migrations.AddField(
            model_name='room',
            name='guests',
            field=models.IntegerField(default=False),
        ),
    ]
