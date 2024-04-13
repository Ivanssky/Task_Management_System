from django.urls import path, include
from .views import create_task, tasks, TaskUpdateView

urlpatterns = [
    path('create/', create_task, name='create task'),
    path('tasks/', tasks, name='tasks'),
    path('tasks/<int:pk>/',include([
        path('edit/', TaskUpdateView.as_view(), name='edit task'),
    ])),
]