from django.contrib import admin
from django.urls import path
from API.views import TodoTaskListCreateView,TodoTaskDetailView

urlpatterns = [
    path('api/task',TodoTaskListCreateView.as_view()),
    path('api/task/<int:pk>',TodoTaskDetailView.as_view()),
    path('admin/', admin.site.urls),

]