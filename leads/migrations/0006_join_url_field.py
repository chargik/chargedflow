# Generated by Django 2.0 on 2017-12-28 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0005_remove_join_url_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='url_field',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
