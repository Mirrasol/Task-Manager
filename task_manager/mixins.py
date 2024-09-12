from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class AuthenticatedMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _('You are not authorized! Please, log in.'))
            return redirect(reverse_lazy('login'))
        return super().dispatch(request, *args, **kwargs)


class OwnerProtectionMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not self.get_object().pk == self.request.user.pk:
            messages.error(request, _('You do not have permissions to edit another user.'))
            return redirect(reverse_lazy('users_index'))
        return super().dispatch(request, *args, **kwargs)


class AuthorProtectionMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not self.get_object().author == self.request.user:
            messages.error(request, _('Task can be deleted only by its author'))
            return redirect(reverse_lazy('tasks_index'))
        return super().dispatch(request, *args, **kwargs)


class DeleteProtectionMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, self.protection_message)
            return redirect(self.protection_redirect)
