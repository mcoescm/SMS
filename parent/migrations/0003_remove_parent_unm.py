# Generated by Django 2.1 on 2018-08-16 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parent', '0002_auto_20180816_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='unm',
        ),
    ]
