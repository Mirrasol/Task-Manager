from django.urls import path
from task_manager.labels.views import (
    IndexView,
    LabelCreateView,
    LabelUpdateView,
)

urlpatterns = [
    path('', IndexView.as_view(), name='labels_index'),
    path('create/', LabelCreateView.as_view(), name='label_create'),
    path('<int:pk>/update/', LabelUpdateView.as_view(), name='label_update'),
]
