# Generated by Django 4.2.6 on 2023-12-13 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0014_alter_student_student_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companyinternship',
            old_name='student',
            new_name='stu',
        ),
        migrations.RenameField(
            model_name='courseinternship',
            old_name='student',
            new_name='stu',
        ),
    ]
