from rest_framework import viewsets
from .models import WeeklySchedule, TimeSlot
from .serializers import WeeklyScheduleSerializer, TimeSlotSerializer
from rest_framework.response import Response
from rest_framework import status

class TimeSlotViewSet(viewsets.ModelViewSet):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer

class WeeklyScheduleViewSet(viewsets.ModelViewSet):
    queryset = WeeklySchedule.objects.all()
    serializer_class = WeeklyScheduleSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Log the validation errors
            print(serializer.errors)  # This will print the errors to the console
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)