# Generated by Django 2.1.1 on 2018-09-28 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_auto_20180914_0833'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentinfo',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='last_name',
            field=models.CharField(default='harun', max_length=50),
            preserve_default=False,
        ),
    ]