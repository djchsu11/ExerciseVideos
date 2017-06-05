# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from Workout.models import Patient


def Index(request):
    return render(request, 'workout/index.html', {'active_tab':'home'})

def Workout(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    print patient
    return render(request, 'workout/workout.html', {'patient' : patient, 'active_tab': 'workout'})
