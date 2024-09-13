from django.views.generic import ListView
from task_manager.labels.models import Label
from task_manager.mixins import AuthenticatedMixin


class IndexView(AuthenticatedMixin, ListView):
    template_name = 'labels/index.html'
    model = Label
    context_object_name = 'labels'
    ordering = ['id']
