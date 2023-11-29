# Generated by Django 4.2.7 on 2023-11-26 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dept_name', models.CharField(choices=[('CS', 'Computer Science'), ('CIS', 'Computer Information Systems'), ('BIT', 'Business Information systems'), ('DS', 'Data Science'), ('AI', 'Artificial Intelligence'), ('CyS', 'Cyber Security')], max_length=30)),
                ('no_of_stud_in_dept', models.PositiveSmallIntegerField(default=0)),
                ('no_of_stu_exceed_90', models.PositiveSmallIntegerField(default=0)),
                ('start', models.DateField(default='')),
                ('end', models.DateField(default='')),
            ],
        ),
    ]
