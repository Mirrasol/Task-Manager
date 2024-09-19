from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class AuthenticatedMixin(LoginRequiredMixin):
    """
    Verify that the user is authenticated.
    Otherwise, send a custom error message and redirect to the login page.
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _('You are not authorized! Please, log in.'))
            return redirect(reverse_lazy('login'))
        return super().dispatch(request, *args, **kwargs)


class OwnerProtectionMixin(LoginRequiredMixin):
    """
    Verify that the user is the current owner of the user profile.
    Otherwise, send a custom error message and redirect to users' list page.
    """
    def dispatch(self, request, *args, **kwargs):
        if not self.get_object().pk == self.request.user.pk:
            messages.error(request, _('You do not have permissions to edit another user.'))
            return redirect(reverse_lazy('users_index'))
        return super().dispatch(request, *args, **kwargs)


class AuthorProtectionMixin(LoginRequiredMixin):
    """
    Verify that the user is the author of the task.
    Otherwise, send a custom error message and redirect to tasks' list page.
    """
    def dispatch(self, request, *args, **kwargs):
        if not self.get_object().author == self.request.user:
            messages.error(request, _('Task can be deleted only by its author'))
            return redirect(reverse_lazy('tasks_index'))
        return super().dispatch(request, *args, **kwargs)


class DeleteProtectionMixin(LoginRequiredMixin):
    """
    Send a custom error message and redirect to a designated page
    in case ProtectedError occurs.
    """
    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, self.protection_message)
            return redirect(self.protection_redirect)
