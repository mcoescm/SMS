# Generated by Django 2.1 on 2018-08-15 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fnm', models.CharField(max_length=40)),
                ('mnm', models.CharField(max_length=40)),
                ('lnm', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=400)),
                ('state', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=40)),
                ('pin', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=40)),
                ('dob', models.DateField()),
                ('age', models.CharField(max_length=3)),
                ('occ', models.CharField(max_length=40)),
                ('phno', models.CharField(max_length=10)),
                ('unm', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('pwd', models.CharField(max_length=40)),
            ],
        ),
    ]
