# Generated by Django 5.1.2 on 2024-10-16 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schedule_app", "0004_alter_timeslot_ids"),
    ]

    operations = [
        migrations.AlterField(
            model_name="timeslot",
            name="ids",
            field=models.JSONField(blank=True, null=True),
        ),
    ]
