# Generated by Django 5.0 on 2023-12-10 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='dept_name',
            field=models.CharField(choices=[('CS', 'Computer Science'), ('CIS', 'Computer Information Systems'), ('BIT', 'Business Information Technology'), ('DS', 'Data Science'), ('AI', 'Artificial Intelligence'), ('CyS', 'Cyber Security')], max_length=30),
        ),
    ]
