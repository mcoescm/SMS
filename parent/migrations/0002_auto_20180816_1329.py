# Generated by Django 2.1 on 2018-08-16 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='email',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]