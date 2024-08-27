from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.urls import reverse_lazy
from task_manager.users.models import User
from task_manager.users.forms import UserCreateForm


class IndexView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        flash = messages.get_messages(request)
        return render(request, 'users/index.html', context={
            'users': users,
            'messages': flash,
        })


class UserCreateView(CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'users/create.html'
    success_url = '/users/'
    success_message = 'User has been registered successfully!'
