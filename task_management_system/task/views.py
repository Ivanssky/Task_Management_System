from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView
from .forms import TaskForm
from .models import Task


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('tasks')

    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})


def tasks(request):
    if request.user.is_authenticated:
        user_tasks = Task.objects.filter(completed=False, user=request.user)
        return render(request, 'tasks/my_tasks.html', {'tasks': user_tasks})


class HomeView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_tasks = Task.objects.filter(completed=False, user=self.request.user)
        last_3_tasks = all_tasks.order_by('created_at')[:3]
        context['last_3_tasks'] = last_3_tasks
        return context


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/edit_task.html'
    success_url = reverse_lazy('tasks')
    context_object_name = 'task'

    def test_func(self):
        task = self.get_object()
        return self.request.user == task.user or self.request.user.is_staff

def mark_as_completed(request, task_id):
    current_page = request.META.get('HTTP_REFERER')
    task = get_object_or_404(Task, pk=task_id)
    task.completed = True
    task.save()
    return redirect(current_page)

def restore_task(request, task_id):
    current_page = request.META.get('HTTP_REFERER')
    task = get_object_or_404(Task, pk=task_id)
    task.completed = False
    task.save()
    return redirect(current_page)

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('completed tasks')

class CompletedTaskView(ListView):
    model = Task
    template_name = 'tasks/completed_tasks.html'
    context_object_name = 'completed_tasks'

    def get_queryset(self):
        return Task.objects.filter(completed=True, user=self.request.user)