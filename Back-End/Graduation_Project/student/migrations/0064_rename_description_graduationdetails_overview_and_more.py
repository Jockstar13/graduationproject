# Generated by Django 5.0 on 2024-01-12 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0063_alter_studentrating_stu_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='graduationdetails',
            old_name='description',
            new_name='overview',
        ),
        migrations.AddField(
            model_name='graduationdetails',
            name='first_paragraph',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='graduationdetails',
            name='first_subtitle',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='graduationdetails',
            name='second_paragraph',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='graduationdetails',
            name='second_subtitle',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='graduationdetails',
            name='weekly_hours',
            field=models.IntegerField(default=0.0),
        ),
    ]
