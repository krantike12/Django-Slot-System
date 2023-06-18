from django.db import models

# Create your models here.
from django.utils import timezone

class Entry(models.Model):
    date_time = models.DateTimeField(default=timezone.now)
    member = models.TextField()
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Slots"