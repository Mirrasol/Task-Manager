from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class CustomPermissionsMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _('You are not authorized! Please, log in.'))
            return redirect(reverse_lazy('login'))
        elif not self.get_object().pk == self.request.user.pk:
            messages.error(request, _('You do not have permissions to edit another user.'))
            return redirect(reverse_lazy('users_index'))
        return super().dispatch(request, *args, **kwargs)
