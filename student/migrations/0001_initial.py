# Generated by Django 2.1.1 on 2018-09-12 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=10)),
                ('fathers_name', models.CharField(max_length=50)),
                ('email', models.TextField()),
                ('mobile_nember', models.IntegerField()),
            ],
        ),
    ]