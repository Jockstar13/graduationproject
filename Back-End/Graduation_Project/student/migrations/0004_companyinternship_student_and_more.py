# Generated by Django 5.0 on 2023-12-10 17:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_companyinternship'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinternship',
            name='student',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.student'),
        ),
        migrations.AlterField(
            model_name='companyinternship',
            name='email',
            field=models.EmailField(max_length=80, verbose_name='Superviser Email'),
        ),
    ]
