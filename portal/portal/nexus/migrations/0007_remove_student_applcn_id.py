# Generated by Django 4.2.5 on 2023-10-24 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nexus', '0006_alter_student_applcn_id_alter_student_diploma_branch_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='Applcn_id',
        ),
    ]
