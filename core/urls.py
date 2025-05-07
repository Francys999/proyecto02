from django.urls import path, include
from rest_framework import routers
from .views import (
    ExerciseViewSet,
    exercise_list,
    exercise_form,
    records_view,   # ← agrégalo
    stats_view      # ← agrégalo
)

router = routers.DefaultRouter()
router.register(r'exercises', ExerciseViewSet, basename='exercise')

urlpatterns = [
    # API DRF
    path('', include(router.urls)),
    # Vistas web básicas
    path('', exercise_list, name='exercise_list'),
    path('new/', exercise_form, name='exercise_new'),
    path('edit/<int:pk>/', exercise_form, name='exercise_edit'),
    path('records/', records_view, name='records'),
    path('stats/', stats_view, name='stats'),
]
