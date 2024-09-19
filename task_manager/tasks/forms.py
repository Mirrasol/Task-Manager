from django.forms import ModelForm
from .models import Task


class TaskForm(ModelForm):
    """
    A custom Task form.
    """
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
