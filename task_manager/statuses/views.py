from django.views.generic import ListView, CreateView, UpdateView
from task_manager.statuses.models import Status
from task_manager.mixins import AuthenticatedMixin
from task_manager.statuses.forms import StatusCreateForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _


class IndexView(AuthenticatedMixin, ListView):
    template_name = 'statuses/index.html'
    model = Status
    context_object_name = 'statuses'
    ordering = ['id']


class StatusCreateView(AuthenticatedMixin, SuccessMessageMixin, CreateView):
    template_name = 'statuses/create.html'
    model = Status
    form_class = StatusCreateForm
    success_url = reverse_lazy('statuses_index')
    success_message = _('Status has been created successfully')


class StatusUpdateView(AuthenticatedMixin, SuccessMessageMixin, UpdateView):
    template_name = 'statuses/update.html'
    model = Status
    form_class = StatusCreateForm
    success_url = reverse_lazy('statuses_index')
    success_message = _('Status has been updated successfully')
