from django.urls import path, include
from .views import create_task, tasks, TaskUpdateView, delete_task, restore_task, mark_as_completed, CompletedTaskView

urlpatterns = [
    path('create/', create_task, name='create task'),
    path('complete/<int:task_id>/', mark_as_completed, name='complete task'),
    path('restore/<int:task_id>/', restore_task, name='restore task'),
    path('delete/<int:task_id>/', delete_task, name='delete task'),
    path('completed-tasks/', CompletedTaskView.as_view(), name='completed tasks'),
    path('tasks/', tasks, name='tasks'),
    path('tasks/<int:pk>/',include([
        path('edit/', TaskUpdateView.as_view(), name='edit task'),




    ])),
]