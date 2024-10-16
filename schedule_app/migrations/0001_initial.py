# Generated by Django 5.1.2 on 2024-10-15 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TimeSlot",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start", models.TimeField()),
                ("stop", models.TimeField()),
                ("ids", models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name="WeeklySchedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "friday",
                    models.ManyToManyField(
                        blank=True,
                        related_name="friday_slots",
                        to="schedule_app.timeslot",
                    ),
                ),
                (
                    "monday",
                    models.ManyToManyField(
                        blank=True,
                        related_name="monday_slots",
                        to="schedule_app.timeslot",
                    ),
                ),
                (
                    "saturday",
                    models.ManyToManyField(
                        blank=True,
                        related_name="saturday_slots",
                        to="schedule_app.timeslot",
                    ),
                ),
                (
                    "sunday",
                    models.ManyToManyField(
                        blank=True,
                        related_name="sunday_slots",
                        to="schedule_app.timeslot",
                    ),
                ),
                (
                    "thursday",
                    models.ManyToManyField(
                        blank=True,
                        related_name="thursday_slots",
                        to="schedule_app.timeslot",
                    ),
                ),
                (
                    "tuesday",
                    models.ManyToManyField(
                        blank=True,
                        related_name="tuesday_slots",
                        to="schedule_app.timeslot",
                    ),
                ),
                (
                    "wednesday",
                    models.ManyToManyField(
                        blank=True,
                        related_name="wednesday_slots",
                        to="schedule_app.timeslot",
                    ),
                ),
            ],
        ),
    ]
