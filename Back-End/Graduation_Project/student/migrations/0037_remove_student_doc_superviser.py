# Generated by Django 5.0 on 2023-12-22 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0036_alter_student_doc_superviser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='doc_superviser',
        ),
    ]
