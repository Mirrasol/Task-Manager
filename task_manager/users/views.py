from django.views.generic import ListView, CreateView
from task_manager.users.models import User
from task_manager.users.forms import UserCreateForm


class IndexView(ListView):
    template_name = 'users/index.html'
    model = User
    context_object_name = 'users'


class UserCreateView(CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'users/create.html'
    success_url = '/users/'
    success_message = 'User has been registered successfully!'
