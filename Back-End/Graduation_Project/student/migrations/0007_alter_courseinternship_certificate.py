# Generated by Django 5.0 on 2023-12-11 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_alter_courseinternship_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseinternship',
            name='certificate',
            field=models.FileField(upload_to='soso/'),
        ),
    ]
