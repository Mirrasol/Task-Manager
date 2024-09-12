from django.urls import path
from task_manager.tasks.views import IndexView, TaskCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='tasks_index'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
]
