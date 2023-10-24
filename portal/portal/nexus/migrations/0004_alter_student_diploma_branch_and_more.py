# Generated by Django 4.2.5 on 2023-10-22 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nexus', '0003_remove_student_user_alter_student_diploma_branch_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Diploma_branch',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='Diploma_college',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='Diploma_percentage',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='student',
            name='Diploma_year_of_passing',
            field=models.PositiveIntegerField(),
        ),
    ]