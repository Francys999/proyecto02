from rest_framework import serializers
from .models import Exercise

class ExerciseSerializer(serializers.ModelSerializer):
    pace = serializers.ReadOnlyField()

    class Meta:
        model = Exercise
        fields = ['id', 'date', 'distance_km', 'time_min', 'pace']
