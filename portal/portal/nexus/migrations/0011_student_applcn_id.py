# Generated by Django 4.2.5 on 2023-10-24 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nexus', '0010_alter_student_s_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Applcn_id',
            field=models.CharField(default='Automatically generated', editable=False, max_length=255),
        ),
    ]