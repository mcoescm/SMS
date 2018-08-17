# Generated by Django 2.1 on 2018-08-17 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.IntegerField(verbose_name=12)),
                ('ispresent', models.IntegerField(default=0, verbose_name=12)),
                ('dt', models.CharField(max_length=40)),
                ('ccid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
        ),
    ]
