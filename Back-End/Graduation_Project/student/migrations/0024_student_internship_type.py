# Generated by Django 5.0 on 2023-12-18 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0023_alter_courseinternship_stu'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='internship_type',
            field=models.CharField(max_length=7, null=True),
        ),
    ]
