# Generated by Django 5.1.1 on 2024-09-07 12:09

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todos", "0007_alter_todomodel_options_alter_todomodel_deadline"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todomodel",
            name="deadline",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 9, 7, 12, 9, 50, 606516, tzinfo=datetime.timezone.utc
                ),
                validators=[
                    django.core.validators.MinValueValidator(
                        limit_value=datetime.datetime(
                            2024, 9, 7, 12, 9, 50, 606535, tzinfo=datetime.timezone.utc
                        )
                    )
                ],
            ),
        ),
    ]
