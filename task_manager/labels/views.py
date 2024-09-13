from django.views.generic import TemplateView
from task_manager.mixins import AuthenticatedMixin


class IndexView(AuthenticatedMixin, TemplateView):
    template_name = 'labels/index.html'
    context_object_name = 'labels'
