# Generated by Django 4.2.5 on 2023-10-24 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nexus', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='S_PRN',
        ),
        migrations.AlterField(
            model_name='application',
            name='application_status',
            field=models.CharField(max_length=20),
        ),
        migrations.AddField(
            model_name='application',
            name='s_prn',
            field=models.CharField(default=0, max_length=20),
        ),
    ]
