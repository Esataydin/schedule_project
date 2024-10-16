from rest_framework import serializers
from .models import WeeklySchedule, TimeSlot

class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = TimeSlot
        fields = ['day', 'start', 'stop', 'ids', 'camera_ids']
        extra_kwargs = {
            'ids': {'required': False},  # Assuming ids are optional
            'camera_ids': {'required': False}  # Assuming camera_ids are optional
        }
class WeeklyScheduleSerializer(serializers.ModelSerializer):
    monday = TimeSlotSerializer(many=True, required=False)
    tuesday = TimeSlotSerializer(many=True, required=False)
    wednesday = TimeSlotSerializer(many=True, required=False)
    thursday = TimeSlotSerializer(many=True, required=False)
    friday = TimeSlotSerializer(many=True, required=False)
    saturday = TimeSlotSerializer(many=True, required=False)
    sunday = TimeSlotSerializer(many=True, required=False)

    class Meta:
        model = WeeklySchedule
        fields = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    def create(self, validated_data):
        # Extract time slots data for each day
        days_data = {
            'monday': validated_data.pop('monday', []),
            'tuesday': validated_data.pop('tuesday', []),
            'wednesday': validated_data.pop('wednesday', []),
            'thursday': validated_data.pop('thursday', []),
            'friday': validated_data.pop('friday', []),
            'saturday': validated_data.pop('saturday', []),
            'sunday': validated_data.pop('sunday', []),
        }

        # Create the WeeklySchedule instance
        weekly_schedule = WeeklySchedule.objects.create(**validated_data)

        # Create TimeSlot instances for each day and associate them with WeeklySchedule
        for day, time_slots in days_data.items():
            for time_slot_data in time_slots:
                time_slot_data['day'] = day  # Set the day
                time_slot = TimeSlot.objects.create(**time_slot_data)
                getattr(weekly_schedule, day).add(time_slot)  # Associate time slot

        return weekly_schedule