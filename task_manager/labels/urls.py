from django.urls import path
from task_manager.labels.views import (
    IndexView,
)

urlpatterns = [
    path('', IndexView.as_view(), name='labels_index'),
]
