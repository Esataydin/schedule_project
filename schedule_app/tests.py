from django.test import TestCase
from rest_framework.test import APIClient
from .models import TimeSlot, WeeklySchedule
import requests

class ScheduleAPITest(TestCase):
    url = "http://127.0.0.1:8000/api/token/refresh/"
    payload = {
        'refresh': YOUR_REFRESH_TOKEN
    }

    response = requests.request("POST", url, data=payload)

    ACCESS_TOKEN = response.json()['access']

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'X-CSRFToken': 'S7JUAs7HYlJH1mfR1jbo4HS2UwAxlXWUmEe0OxIWBIF8kVyCDGiL3DXH23itV8Zw'
    }

    def setUp(self):
        self.client = APIClient()


    def test_create_timeslot(self):
        data = {
                    "start": "00:00",
                    "stop": "01:00",
                    "ids": [1]
            }
        response = self.client.post('/api/timeslots/', data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_get_weekly_schedule(self):
        response = self.client.get('/api/weekly_schedule/')
        self.assertEqual(response.status_code, 200)
