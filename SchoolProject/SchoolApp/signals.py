from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
from django.utils import timezone


@receiver(post_save, sender=SubjectModel)
def calculate_percentage_of_student(sender, instance, created, **kwargs):
    if created:
        student = instance.child
        marks = SubjectModel.objects.filter(child=student)
        total_marks = sum([getattr(instance, field) for field in ['english', 'mathematics', 'chemistry', 'biology', 'history', 'geography', 'politics']])
        percentage = round((total_marks / 700) * 100, 2)
        historical_percentage, _ = historicalData.objects.update_or_create(
            child=student,
            defaults={
                'year': timezone.now(),
                'percentage': percentage
            }
        )