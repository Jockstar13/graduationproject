# Generated by Django 5.0 on 2023-12-29 16:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0050_remove_graduationproject_superviser_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeline',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.graduationproject'),
        ),
    ]
