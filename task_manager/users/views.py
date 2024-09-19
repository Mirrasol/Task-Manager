from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from task_manager.users.forms import UserForm
from task_manager.mixins import AuthenticatedMixin, OwnerProtectionMixin, DeleteProtectionMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _


class IndexView(ListView):
    """
    View for the list of registered users.
    """
    template_name = 'users/index.html'
    model = get_user_model()
    context_object_name = 'users'
    ordering = ['id']


class UserCreateView(SuccessMessageMixin, CreateView):
    """
    View for creating a new user, based on CreateView class.
    Specifies a custom success message and redirects to login page.
    """
    template_name = 'users/create.html'
    model = get_user_model()
    form_class = UserForm
    success_url = reverse_lazy('login')
    success_message = _('User has been registered successfully')


class UserUpdateView(
    AuthenticatedMixin,
    OwnerProtectionMixin,
    SuccessMessageMixin,
    UpdateView,
):
    """
    View for updating a user, based on UpdateView class.
    Verifies that the current user is authorized.
    Specifies a custom success message and redirects to users' list page.
    """
    template_name = 'users/update.html'
    model = get_user_model()
    form_class = UserForm
    success_url = reverse_lazy('users_index')
    success_message = _('User has been updated successfully')


class UserDeleteView(
    AuthenticatedMixin,
    OwnerProtectionMixin,
    DeleteProtectionMixin,
    SuccessMessageMixin,
    DeleteView,
):
    """
    View for deleting a user, based on DeleteView class.
    Verifies that the current user is authorized.
    In case of success, specifies a custom success message.
    Otherwise, specifies a custom error message.
    Redirects to users' list page.
    """
    template_name = 'users/delete.html'
    model = get_user_model()
    success_url = reverse_lazy('users_index')
    success_message = _('User has been deleted successfully')
    protection_message = _('Cannot delete user that is currently being used')
    protection_redirect = reverse_lazy('users_index')
