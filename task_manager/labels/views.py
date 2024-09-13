from django.views.generic import ListView, CreateView
from task_manager.labels.models import Label
from task_manager.labels.forms import LabelCreateForm
from task_manager.mixins import AuthenticatedMixin
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _


class IndexView(AuthenticatedMixin, ListView):
    template_name = 'labels/index.html'
    model = Label
    context_object_name = 'labels'
    ordering = ['id']


class LabelCreateView(AuthenticatedMixin, SuccessMessageMixin, CreateView):
    template_name = 'labels/create.html'
    model = Label
    form_class = LabelCreateForm
    success_url = reverse_lazy('labels_index')
    success_message = _('Label has been created successfully')
