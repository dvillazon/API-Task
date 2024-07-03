from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField( max_length= 200)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
