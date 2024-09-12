from django.views.generic import ListView
from task_manager.tasks.models import Task
from task_manager.mixins import AuthenticatedMixin


class IndexView(AuthenticatedMixin, ListView):
    template_name = 'tasks/index.html'
    model = Task
    context_object_name = 'tasks'
    ordering = ['id']
