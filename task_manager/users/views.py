from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from task_manager.users.forms import UserCreateForm
from task_manager.mixins import AuthenticatedMixin, OwnerProtectionMixin, DeleteProtectionMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _


class IndexView(ListView):
    template_name = 'users/index.html'
    model = get_user_model()
    context_object_name = 'users'
    ordering = ['id']


class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = 'users/create.html'
    model = get_user_model()
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    success_message = _('User has been registered successfully')


class UserUpdateView(
    AuthenticatedMixin,
    OwnerProtectionMixin,
    SuccessMessageMixin,
    UpdateView,
):
    template_name = 'users/update.html'
    model = get_user_model()
    form_class = UserCreateForm
    success_url = reverse_lazy('users_index')
    success_message = _('User has been updated successfully')


class UserDeleteView(
    AuthenticatedMixin,
    OwnerProtectionMixin,
    DeleteProtectionMixin,
    SuccessMessageMixin,
    DeleteView,
):
    template_name = 'users/delete.html'
    model = get_user_model()
    success_url = reverse_lazy('users_index')
    success_message = _('User has been deleted successfully')
    protection_message = _('Cannot delete user that is currently being used')
    protection_redirect = reverse_lazy('users_index')
