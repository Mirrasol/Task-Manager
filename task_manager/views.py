from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm


class Homepage(TemplateView):
    template_name = 'homepage.html'


class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
