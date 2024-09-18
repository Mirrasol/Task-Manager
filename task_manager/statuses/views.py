from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.statuses.models import Status
from task_manager.mixins import AuthenticatedMixin, DeleteProtectionMixin
from task_manager.statuses.forms import StatusForm
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
    form_class = StatusForm
    success_url = reverse_lazy('statuses_index')
    success_message = _('Status has been created successfully')


class StatusUpdateView(AuthenticatedMixin, SuccessMessageMixin, UpdateView):
    template_name = 'statuses/update.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses_index')
    success_message = _('Status has been updated successfully')


class StatusDeleteView(AuthenticatedMixin, DeleteProtectionMixin, SuccessMessageMixin, DeleteView):
    template_name = 'statuses/delete.html'
    model = Status
    success_url = reverse_lazy('statuses_index')
    success_message = _('Status has been deleted successfully')
    protection_message = _('Cannot delete status that is currently being used')
    protection_redirect = reverse_lazy('statuses_index')
