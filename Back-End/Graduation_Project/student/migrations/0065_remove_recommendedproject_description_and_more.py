# Generated by Django 5.0 on 2024-01-12 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0064_rename_description_graduationdetails_overview_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recommendedproject',
            name='description',
        ),
        migrations.RemoveField(
            model_name='recommendedproject',
            name='title_sub',
        ),
        migrations.RemoveField(
            model_name='recommendedproject',
            name='weekly_hours',
        ),
    ]