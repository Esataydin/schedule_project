from django.db import models

class TimeSlot(models.Model):
    day = models.CharField(max_length=9, default='monday')  # e.g., "monday", "tuesday", etc.
    start = models.TimeField()
    stop = models.TimeField()
    ids = models.JSONField(null=True, blank=True)  # Stores the list of IDs for that time slot.
    camera_ids = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.day}: {self.start} - {self.stop}"
class WeeklySchedule(models.Model):
    monday = models.ManyToManyField(TimeSlot, related_name='monday_slots', blank=True)
    tuesday = models.ManyToManyField(TimeSlot, related_name='tuesday_slots', blank=True)
    wednesday = models.ManyToManyField(TimeSlot, related_name='wednesday_slots', blank=True)
    thursday = models.ManyToManyField(TimeSlot, related_name='thursday_slots', blank=True)
    friday = models.ManyToManyField(TimeSlot, related_name='friday_slots', blank=True)
    saturday = models.ManyToManyField(TimeSlot, related_name='saturday_slots', blank=True)
    sunday = models.ManyToManyField(TimeSlot, related_name='sunday_slots', blank=True)
