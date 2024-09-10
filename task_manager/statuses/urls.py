from django.urls import path
from task_manager.statuses.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='statuses_index'),
]
