# Generated by Django 5.0.2 on 2024-03-02 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rename_session_id_student_session_year_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.TextField(),
        ),
    ]
