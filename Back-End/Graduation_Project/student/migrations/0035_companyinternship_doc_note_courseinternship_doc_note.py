# Generated by Django 5.0 on 2023-12-22 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0034_remove_companyinternship_doc_note_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinternship',
            name='doc_note',
            field=models.TextField(default='Ther is no Notes', max_length=450, null=True),
        ),
        migrations.AddField(
            model_name='courseinternship',
            name='doc_note',
            field=models.TextField(default='Ther is no Notes', max_length=450, null=True),
        ),
    ]
