# Generated by Django 5.0 on 2023-12-26 11:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0043_alter_graduationproject_project_type'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='graduationproject',
            name='project_type',
            field=models.CharField(max_length=12),
        ),
        migrations.RemoveField(
            model_name='graduationproject',
            name='stu_gp',
        ),
        migrations.AddField(
            model_name='graduationproject',
            name='stu_gp',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]