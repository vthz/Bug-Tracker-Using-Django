# Generated by Django 3.2.5 on 2021-07-18 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bug_Tracker_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug_table',
            name='project_id',
            field=models.CharField(max_length=20),
        ),
    ]
