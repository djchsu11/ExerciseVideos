# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Patient(models.Model):
    patient_loginName = models.CharField(max_length=36)
    workout_start_date = models.DateTimeField('date started')
    workout_end_date = models.DateTimeField('date finished')

    def __str__(self):
        return self.patient_loginName

class Exercise(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    exercise_name = models.CharField(max_length=200)
    video_link = models.CharField(max_length=500)

    def __str__(self):
        return self.exercise_name

