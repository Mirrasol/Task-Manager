from django.urls import path
from task_manager.tasks.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='tasks_index'),
]
