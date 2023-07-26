from django.shortcuts import render
from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer
from . pagination import SmallSetPagination


# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    pagination_class = SmallSetPagination
    
    def get_queryset(self):
        queryset = Todo.objects.all()
        return queryset
        