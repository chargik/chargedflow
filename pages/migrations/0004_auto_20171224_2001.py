# Generated by Django 2.0 on 2017-12-24 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20171219_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tours',
            name='category',
            field=models.CharField(choices=[('bus', 'Bus'), ('avia', 'Avia'), ('ind', 'Individual'), ('corp', 'Corporate')], default='bus', max_length=20),
        ),
    ]
