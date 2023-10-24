# Generated by Django 4.2.5 on 2023-10-24 11:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('nexus', '0015_alter_notice_notice_type_alter_notice_uploaded_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notice',
            old_name='description',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='title',
        ),
        migrations.AddField(
            model_name='notice',
            name='notice_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='notice',
            name='uploaded_by',
            field=models.ForeignKey(default='user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
