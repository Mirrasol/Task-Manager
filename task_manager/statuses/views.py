from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.statuses.models import Status
from task_manager.mixins import AuthenticatedMixin, DeleteProtectionMixin
from task_manager.statuses.forms import StatusForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _


class IndexView(AuthenticatedMixin, ListView):
    """
    View for the list of statuses.
    Verifies that the viewer is authorized.
    """
    template_name = 'statuses/index.html'
    model = Status
    context_object_name = 'statuses'
    ordering = ['id']


class StatusCreateView(AuthenticatedMixin, SuccessMessageMixin, CreateView):
    """
    View for creating a new status, based on CreateView class.
    Verifies that the current user is authorized.
    Specifies a custom success message and redirects to statuses' list page.
    """
    template_name = 'statuses/create.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses_index')
    success_message = _('Status has been created successfully')


class StatusUpdateView(AuthenticatedMixin, SuccessMessageMixin, UpdateView):
    """
    View for updating a status, based on UpdateView class.
    Verifies that the current user is authorized.
    Specifies a custom success message and redirects to statuses' list page.
    """
    template_name = 'statuses/update.html'
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('statuses_index')
    success_message = _('Status has been updated successfully')


class StatusDeleteView(AuthenticatedMixin, DeleteProtectionMixin, SuccessMessageMixin, DeleteView):
    """
    View for deleting a status, based on DeleteView class.
    Verifies that the current user is authorized.
    In case of success, specifies a custom success message.
    Otherwise, specifies a custom error message.
    Redirects to statuses' list page.
    """
    template_name = 'statuses/delete.html'
    model = Status
    success_url = reverse_lazy('statuses_index')
    success_message = _('Status has been deleted successfully')
    protection_message = _('Cannot delete status that is currently being used')
    protection_redirect = reverse_lazy('statuses_index')
