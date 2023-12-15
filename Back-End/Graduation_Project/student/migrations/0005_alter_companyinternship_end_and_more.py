# Generated by Django 5.0 on 2023-12-11 09:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_companyinternship_student_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyinternship',
            name='end',
            field=models.DateField(verbose_name='Ending Date'),
        ),
        migrations.AlterField(
            model_name='companyinternship',
            name='start',
            field=models.DateField(verbose_name='starting Date'),
        ),
        migrations.CreateModel(
            name='CourseInternship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=80, verbose_name='Course Name')),
                ('hour', models.PositiveSmallIntegerField()),
                ('provider', models.CharField(max_length=80, verbose_name='Course Provider')),
                ('certificate', models.FileField(upload_to='')),
                ('student', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]