# Generated by Django 4.2.5 on 2023-10-26 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nexus', '0003_remove_coordinator_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='S_PRN',
            field=models.PositiveIntegerField(max_length=15, unique=True),
        ),
    ]
