from django.shortcuts import render, get_object_or_404, redirect
from django.db import models
from rest_framework import viewsets
from .models import Exercise
from .serializers import ExerciseSerializer
from .forms import ExerciseForm

# ———————— VISTAS WEB ————————

def exercise_list(request):
    exercises = Exercise.objects.order_by('-date')
    return render(request, 'core/exercise_list.html', {'exercises': exercises})

def exercise_form(request, pk=None):
    instance = get_object_or_404(Exercise, pk=pk) if pk else None
    form = ExerciseForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('exercise_list')
    return render(request, 'core/exercise_form.html', {'form': form})

def records_view(request):
    best_pace    = Exercise.objects.aggregate(min_pace=models.Min('pace'))['min_pace']
    max_distance = Exercise.objects.aggregate(max_dist=models.Max('distance_km'))['max_dist']
    return render(request, 'core/records.html', {
        'best_pace': best_pace,
        'max_distance': max_distance
    })

def stats_view(request):
    total_runs     = Exercise.objects.count()
    total_distance = Exercise.objects.aggregate(sum_dist=models.Sum('distance_km'))['sum_dist'] or 0
    average_pace   = Exercise.objects.aggregate(avg_pace=models.Avg('pace'))['avg_pace'] or 0
    return render(request, 'core/stats.html', {
        'total_runs': total_runs,
        'total_distance': total_distance,
        'average_pace': average_pace
    })

# ———————— API DRF ————————

class ExerciseViewSet(viewsets.ModelViewSet):
    """
    CRUD completo de Exercise vía API REST
    """
    queryset = Exercise.objects.order_by('-date')
    serializer_class = ExerciseSerializer

    # Si quieres los endpoints /exercises/records/ y /exercises/stats/,
    # descomenta este ejemplo e importa @action y Response:
    #
    # from rest_framework.decorators import action
    # from rest_framework.response import Response
    #
    # @action(detail=False)
    # def records(self, request):
    #     data = {
    #         'best_pace': Exercise.objects.aggregate(models.Min('pace'))['pace__min'],
    #         'max_dist' : Exercise.objects.aggregate(models.Max('distance_km'))['distance_km__max'],
    #     }
    #     return Response(data)
    #
    # @action(detail=False)
    # def stats(self, request):
    #     data = {
    #         'total_runs': Exercise.objects.count(),
    #         'total_distance': Exercise.objects.aggregate(models.Sum('distance_km'))['distance_km__sum'],
    #         'avg_pace': Exercise.objects.aggregate(models.Avg('pace'))['pace__avg'],
    #     }
    #     return Response(data)
