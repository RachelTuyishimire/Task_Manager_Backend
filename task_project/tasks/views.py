from django.shortcuts import render

from rest_framework import viewsets, status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.utils import timezone

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    
    queryset = Task.objects.all().order_by('-created_at')

    # def get_queryset(self):
    #     # Check for overdue tasks
    #     user_tasks = Task.objects.filter(user=self.request.user)
    #     for task in user_tasks.filter(status='todo'):
    #         if task.due_date < timezone.now():
    #             task.status = 'overdue'
    #             task.save()
    #     return user_tasks
    
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


