from django.views.generic import ListView, CreateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from task_manager.users.forms import UserCreateForm


class IndexView(ListView):
    template_name = 'users/index.html'
    model = get_user_model()
    context_object_name = 'users'


class UserCreateView(CreateView):
    template_name = 'users/create.html'
    model = get_user_model()
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
