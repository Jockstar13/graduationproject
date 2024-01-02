# Generated by Django 5.0 on 2023-12-20 21:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0025_rename_hours_weeklyfollowing_hour_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='weeklyfollowing',
            name='stu_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='weeklyfollowing',
            name='week',
            field=models.CharField(max_length=6, null=True),
        ),
    ]