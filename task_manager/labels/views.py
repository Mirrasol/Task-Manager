from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.labels.models import Label
from task_manager.labels.forms import LabelForm
from task_manager.mixins import AuthenticatedMixin, DeleteProtectionMixin
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _


class IndexView(AuthenticatedMixin, ListView):
    """
    View for the list of labels.
    Verifies that the viewer is authorized.
    """
    template_name = 'labels/index.html'
    model = Label
    context_object_name = 'labels'
    ordering = ['id']


class LabelCreateView(AuthenticatedMixin, SuccessMessageMixin, CreateView):
    """
    View for creating a new label, based on CreateView class.
    Verifies that the current user is authorized.
    Specifies a custom success message and redirects to labels' list page.
    """
    template_name = 'labels/create.html'
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels_index')
    success_message = _('Label has been created successfully')


class LabelUpdateView(AuthenticatedMixin, SuccessMessageMixin, UpdateView):
    """
    View for updating a label, based on UpdateView class.
    Verifies that the current user is authorized.
    Specifies a custom success message and redirects to labels' list page.
    """
    template_name = 'labels/update.html'
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels_index')
    success_message = _('Label has been updated successfully')


class LabelDeleteView(AuthenticatedMixin, DeleteProtectionMixin, SuccessMessageMixin, DeleteView):
    """
    View for deleting a label, based on DeleteView class.
    Verifies that the current user is authorized.
    In case of success, specifies a custom success message.
    Otherwise, specifies a custom error message.
    Redirects to labels' list page.
    """
    template_name = 'labels/delete.html'
    model = Label
    success_url = reverse_lazy('labels_index')
    success_message = _('Label has been deleted successfully')
    protection_message = _('Cannot delete label that is currently being used')
    protection_redirect = reverse_lazy('labels_index')
