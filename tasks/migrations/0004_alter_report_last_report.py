# Generated by Django 3.2.12 on 2022-03-13 15:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_report_last_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='last_report',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 13, 0, 18, 56, 175958, tzinfo=utc), null=True),
        ),
    ]
