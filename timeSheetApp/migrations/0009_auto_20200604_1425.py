# Generated by Django 2.2 on 2020-06-04 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeSheetApp', '0008_auto_20200604_1417'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Admin',
            new_name='AdminRole',
        ),
    ]