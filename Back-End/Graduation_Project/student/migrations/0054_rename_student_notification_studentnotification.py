# Generated by Django 5.0 on 2023-12-31 16:45

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0053_alter_timeline_team_student_notification'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='student_notification',
            new_name='StudentNotification',
        ),
    ]