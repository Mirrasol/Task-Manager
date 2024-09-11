from django.urls import path
from task_manager.statuses.views import IndexView, StatusCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='statuses_index'),
    path('create/', StatusCreateView.as_view(), name='status_create'),
]
