# Generated by Django 5.0 on 2023-12-24 13:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0039_alter_student_doc_superviser'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseinternship',
            name='certificate',
            field=models.FileField(null=True, upload_to='Files/Internship/Courses/%Y/%B'),
        ),
        migrations.CreateModel(
            name='GraduationProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=32)),
                ('semester', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=32)),
                ('major', models.CharField(max_length=32)),
                ('stu_id', models.CharField(max_length=12)),
                ('superviser', models.CharField(max_length=32)),
                ('project_type', models.CharField(max_length=12)),
                ('project_name', models.CharField(max_length=128)),
                ('project_idea', models.CharField(max_length=720)),
                ('project_goal', models.CharField(max_length=400)),
                ('technologies', models.CharField(max_length=400)),
                ('stu_gp', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
