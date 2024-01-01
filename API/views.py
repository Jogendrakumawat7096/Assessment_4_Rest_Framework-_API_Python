from rest_framework import generics
from .models import TodoTask
from .serializers import TodoTaskSerializer

class TodoTaskListCreateView(generics.ListCreateAPIView):
    queryset = TodoTask.objects.all()
    serializer_class = TodoTaskSerializer

class TodoTaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoTask.objects.all()
    serializer_class = TodoTaskSerializer