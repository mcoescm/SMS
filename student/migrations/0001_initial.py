# Generated by Django 2.1 on 2018-08-15 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentreg',
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
                ('email', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=10)),
                ('username', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
                ('parent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parent.parentreg')),
            ],
        ),
    ]
