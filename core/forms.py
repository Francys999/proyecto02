from django import forms
from .models import Exercise

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['date', 'distance_km', 'time_min']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
