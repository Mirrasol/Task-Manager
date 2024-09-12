from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.tasks.models import Task
from task_manager.mixins import AuthenticatedMixin, AuthorProtectionMixin
from task_manager.tasks.forms import TaskCreateForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _


class IndexView(AuthenticatedMixin, ListView):
    template_name = 'tasks/index.html'
    model = Task
    context_object_name = 'tasks'
    ordering = ['id']


class TaskCreateView(AuthenticatedMixin, SuccessMessageMixin, CreateView):
    template_name = 'tasks/create.html'
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy('tasks_index')
    success_message = _('Task has been created successfully')

    def form_valid(self, form):
        task = form.save(commit=False)
        task.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(AuthenticatedMixin, SuccessMessageMixin, UpdateView):
    template_name = 'tasks/update.html'
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy('tasks_index')
    success_message = _('Task has been updated successfully')


class TaskDeleteView(AuthenticatedMixin, AuthorProtectionMixin, SuccessMessageMixin, DeleteView):
    template_name = 'tasks/delete.html'
    model = Task
    success_url = reverse_lazy('tasks_index')
    success_message = _('Task has been deleted successfully')