# Generated by Django 5.0 on 2023-12-22 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0032_alter_courseinternship_doc_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyinternship',
            name='doc_note',
            field=models.TextField(default='Ther is no Notes', max_length=450, null=True),
        ),
    ]