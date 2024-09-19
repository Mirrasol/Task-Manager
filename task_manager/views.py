from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _


class Homepage(TemplateView):
    template_name = 'homepage.html'


class CustomLoginView(SuccessMessageMixin, LoginView):
    """
    Add a custom message for a successful user login.
    """
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_message = _('You are logged in')


class CustomLogoutView(LogoutView):
    """
    Add a custom message for a successful user logout.
    """
    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('You are logged out'))
        return super().dispatch(request, *args, **kwargs)
