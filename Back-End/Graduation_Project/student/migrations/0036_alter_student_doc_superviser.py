# Generated by Django 5.0 on 2023-12-22 17:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0007_remove_doctor_type'),
        ('student', '0035_companyinternship_doc_note_courseinternship_doc_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='doc_superviser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor'),
        ),
    ]