# Generated by Django 2.0 on 2017-12-11 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tours',
            options={'ordering': ['-timestamp', '-updated'], 'verbose_name_plural': 'tours'},
        ),
    ]