from django.db import models

from django.db import models
from django.contrib.auth.models import User # type: ignore
from django.utils import timezone

class Task(models.Model):
    STATUS_CHOICES = (
        ('todo', 'To Do'),
        ('done', 'Done'),
        ('overdue', 'Overdue'),
    )
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='todo')
    
    
    def save(self, *args, **kwargs):
        # Check if task is overdue
        if self.due_date < timezone.now() and self.status == 'todo':
            self.status = 'overdue'
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title