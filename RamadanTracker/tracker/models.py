# tracker/models.py

from django.db import models

class Record(models.Model):
    date = models.DateField()
    day = models.CharField(max_length=255)
    quran_recitation = models.TextField()
    fajr = models.BooleanField(default=False)
    dhuhr = models.BooleanField(default=False)
    asr = models.BooleanField(default=False)
    maghrib = models.BooleanField(default=False)
    isha = models.BooleanField(default=False)
    tahajjud = models.BooleanField(default=False)
