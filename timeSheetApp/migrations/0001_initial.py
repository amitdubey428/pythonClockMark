# Generated by Django 2.2 on 2020-06-03 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('project_title', models.CharField(max_length=250)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('email_id', models.EmailField(max_length=254, unique=True)),
                ('phone_no', models.CharField(max_length=12)),
                ('roles', models.CharField(choices=[('PM', 'Project Manager'), ('SM', 'Scheduling Manager'), ('PC', 'Project Collaborator')], max_length=2)),
                ('working_hours_start', models.TimeField()),
                ('working_hours_end', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('task_title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('task_status', models.CharField(choices=[('S', 'Started'), ('O', 'On going'), ('C', 'Completed')], max_length=1)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timeSheetApp.Project')),
            ],
        ),
    ]
