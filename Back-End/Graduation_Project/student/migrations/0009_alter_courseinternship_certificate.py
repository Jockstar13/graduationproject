# Generated by Django 5.0 on 2023-12-11 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_alter_courseinternship_certificate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseinternship',
            name='certificate',
            field=models.FileField(null=True, upload_to='static'),
        ),
    ]
