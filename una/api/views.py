import csv
import logging
from datetime import datetime
from io import StringIO

from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from una.api.helpers import safe_cast_int
from una.api.models import GlucoseData
from una.api.serializers import GlucoseDataSerializer, FileUploadSerializer


logger = logging.getLogger(__name__)


class GlucoseDataView(ReadOnlyModelViewSet):
    queryset = GlucoseData.objects.all()
    serializer_class = GlucoseDataSerializer
    lookup_field = 'id'

    filterset_fields = {
        'device_timestamp': ['gte', 'lte'],
        'user_id': ['exact']
    }


def process_glucose_data(user_id, content):
    reader = csv.reader(content, delimiter=",")
    glucose_data_list = []

    for row in reader:
        try:
            glucose_data_list.append(GlucoseData(
                user_id=user_id,
                device=row[0],
                serial_number=row[1],
                device_timestamp=datetime.strptime(row[2], "%d-%m-%Y %H:%M"),
                recording_type=safe_cast_int(row[3]),
                glucose_value_history=safe_cast_int(row[4]),
                glucose_scan=safe_cast_int(row[5]),
                rapid_acting_insulin=row[6],
                rapid_insulin=safe_cast_int(row[7]),
                nutritional_data=row[8],
                carbohydrates_gram=safe_cast_int(row[9]),
                carbohydrates_servings=safe_cast_int(row[10]),
                depot_insulin=row[11],
                depot_insulin_units=safe_cast_int(row[12]),
                notes=row[13],
                glucose_test_strips=safe_cast_int(row[13]),
                ketone=safe_cast_int(row[14]),
                meal_insulin=safe_cast_int(row[15]),
                correction_insulin=safe_cast_int(row[16]),
                user_insulin_change=safe_cast_int(row[17])
            ))
        except Exception:
            logger.warning(f'Error occurred while importing row from file {user_id}.csv')
    GlucoseData.objects.bulk_create(glucose_data_list)


class ImportGlucoseData(CreateAPIView):
    serializer_class = FileUploadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_file = serializer.validated_data['file']
        user_id = validated_file.name.split('.')[0]
        content = StringIO(validated_file.read().decode('utf-8'))
        process_glucose_data(user_id, content)

        return Response({"status": "success"},
                        status.HTTP_201_CREATED)


