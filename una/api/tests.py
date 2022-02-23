import datetime

from django.test import TestCase
from rest_framework.test import APIClient

from una.api.models import GlucoseData


class GlucoseDataViewSetTestCase(TestCase):

    def setUp(self):
        self.api_client = APIClient()
        glucose_data_list = []
        for i in range(0, 100):
            glucose_data_list.append(GlucoseData(
                user_id='tttt-ttttt-ttttt',
                device='device',
                serial_number='e09bb0f0-018b-429b-94c7-62bb306a0136',
                device_timestamp=datetime.datetime(2017, 12, 22),
                recording_type=i,
                glucose_value_history=150,
                glucose_scan=None,
                rapid_acting_insulin='',
                rapid_insulin=None,
                nutritional_data='',
                carbohydrates_gram=None,
                carbohydrates_servings=None,
                depot_insulin='',
                depot_insulin_units=None,
                notes='',
                glucose_test_strips=None,
                ketone=None,
                meal_insulin=None,
                correction_insulin=None,
                user_insulin_change=None
            )
        )
        GlucoseData.objects.bulk_create(glucose_data_list)
        self.glucose_data = GlucoseData.objects.get(id=1)
        self.glucose_data_list = GlucoseData.objects.all()

    def test_view_retrieve(self):
        response = self.api_client.get(f'/api/v1/levels/{self.glucose_data.id}/')
        self.assertEqual(response.status_code, 200)
        expected_json = {'id': 1, 'user_id': 'tttt-ttttt-ttttt', 'device': 'device',
                         'serial_number': 'e09bb0f0-018b-429b-94c7-62bb306a0136',
                         'device_timestamp': '2017-12-22T00:00:00Z', 'recording_type': 0, 'glucose_value_history': 150,
                         'glucose_scan': None, 'rapid_acting_insulin': '', 'rapid_insulin': None,
                         'nutritional_data': '', 'carbohydrates_gram': None, 'carbohydrates_servings': None,
                         'depot_insulin': '', 'depot_insulin_units': None, 'notes': '', 'glucose_test_strips': None,
                         'ketone': None, 'meal_insulin': None, 'correction_insulin': None, 'user_insulin_change': None}

        self.assertDictEqual(response.json(), expected_json)

    def test_view_list(self):
        response = self.api_client.get(f'/api/v1/levels/')
        response_json = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response_json['results']), 100)

        response = self.api_client.get(f'/api/v1/levels/?limit=50')
        response_json = response.json()
        self.assertEqual(len(response_json['results']), 50)

        response = self.api_client.get(f'/api/v1/levels/?limit=50')
        response_json = response.json()
        self.assertEqual(len(response_json['results']), 50)

        glucose_data = GlucoseData.objects.get(id=1)
        glucose_data.user_id = 'jjj-jjj-jjj'
        glucose_data.save()

        response = self.api_client.get(f'/api/v1/levels/?user_id={glucose_data.user_id}')
        response_json = response.json()
        self.assertEqual(len(response_json['results']), 1)