from django.urls import path
from task_manager.labels.views import (
    IndexView,
    LabelCreateView,
)

urlpatterns = [
    path('', IndexView.as_view(), name='labels_index'),
    path('create/', LabelCreateView.as_view(), name='label_create'),
]
