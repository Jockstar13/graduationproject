# Generated by Django 5.0 on 2023-12-31 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0009_rename_doctor_notification_doctornotification'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctornotification',
            name='query_pk',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='doctornotification',
            name='url_name',
            field=models.CharField(max_length=24, null=True),
        ),
    ]
