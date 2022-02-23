from django.contrib.auth.models import User
from django.db import models


class GlucoseData(models.Model):
    """Model to represent Glucose Data"""

    user_id = models.CharField(max_length=100)
    device = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    device_timestamp = models.DateTimeField()
    recording_type = models.IntegerField(blank=True, null=True)
    glucose_value_history = models.IntegerField(blank=True, null=True)
    glucose_scan = models.IntegerField(blank=True, null=True)
    rapid_acting_insulin = models.CharField(max_length=100)
    rapid_insulin = models.IntegerField(blank=True, null=True)
    nutritional_data = models.CharField(max_length=100)
    carbohydrates_gram = models.IntegerField(blank=True, null=True)
    carbohydrates_servings = models.IntegerField(blank=True, null=True)
    depot_insulin = models.CharField(max_length=100)
    depot_insulin_units = models.IntegerField(blank=True, null=True)
    notes = models.CharField(max_length=100)
    glucose_test_strips = models.IntegerField(blank=True, null=True)
    ketone = models.IntegerField(blank=True, null=True)
    meal_insulin = models.IntegerField(blank=True, null=True)
    correction_insulin = models.IntegerField(blank=True, null=True)
    user_insulin_change = models.IntegerField(blank=True, null=True)
