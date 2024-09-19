from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django_filters.views import FilterView
from task_manager.tasks.models import Task
from task_manager.tasks.filters import TaskFilter
from task_manager.tasks.forms import TaskForm
from task_manager.mixins import AuthenticatedMixin, AuthorProtectionMixin
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _


class IndexView(AuthenticatedMixin, FilterView, ListView):
    """
    View for the list of tasks.
    Verifies that the viewer is authorized.
    """
    template_name = 'tasks/index.html'
    model = Task
    filterset_class = TaskFilter
    context_object_name = 'tasks'
    ordering = ['id']


class TaskCreateView(AuthenticatedMixin, SuccessMessageMixin, CreateView):
    """
    View for creating a new task, based on CreateView class.
    Verifies that the current user is authorized.
    Specifies a custom success message and redirects to tasks' list page.
    """
    template_name = 'tasks/create.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks_index')
    success_message = _('Task has been created successfully')

    def form_valid(self, form):
        task = form.save(commit=False)
        task.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(AuthenticatedMixin, SuccessMessageMixin, UpdateView):
    """
    View for updating a task, based on UpdateView class.
    Verifies that the current user is authorized.
    Specifies a custom success message and redirects to tasks' list page.
    """
    template_name = 'tasks/update.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks_index')
    success_message = _('Task has been updated successfully')


class TaskDeleteView(AuthenticatedMixin, AuthorProtectionMixin, SuccessMessageMixin, DeleteView):
    """
    View for deleting a task, based on DeleteView class.
    Verifies that the current user is authorized.
    Specifies a custom success message and redirects to tasks' list page.
    """
    template_name = 'tasks/delete.html'
    model = Task
    success_url = reverse_lazy('tasks_index')
    success_message = _('Task has been deleted successfully')


class TaskView(AuthenticatedMixin, DetailView):
    """
    View for a particular task.
    Verifies that the viewer is authorized.
    """
    template_name = 'tasks/overview.html'
    model = Task
