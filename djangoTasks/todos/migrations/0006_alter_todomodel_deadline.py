# Generated by Django 5.1.1 on 2024-09-07 11:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todos", "0005_alter_todomodel_deadline"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todomodel",
            name="deadline",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 9, 7, 11, 48, 46, 57065, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
