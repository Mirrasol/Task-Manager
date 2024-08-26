from django.shortcuts import render
from django.views import View
from task_manager.users.models import Users


class IndexView(View):
    def get(self, request, *args, **kwargs):
        users = Users.objects.all()
        return render(request, 'users/index.html', context={
            'users': users
        })
