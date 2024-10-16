from rest_framework.routers import DefaultRouter
from .views import TimeSlotViewSet, WeeklyScheduleViewSet

router = DefaultRouter()
router.register(r'timeslots', TimeSlotViewSet)
router.register(r'weekly_schedule', WeeklyScheduleViewSet)

urlpatterns = router.urls
