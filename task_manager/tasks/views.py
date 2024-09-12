from django.views.generic import TemplateView
from task_manager.mixins import AuthenticatedMixin


class IndexView(AuthenticatedMixin, TemplateView):
    template_name = 'statuses/index.html'
    context_object_name = 'tasks'
