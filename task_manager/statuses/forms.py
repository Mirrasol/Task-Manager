from django.forms import ModelForm
from .models import Status


class StatusForm(ModelForm):
    """
    A custom Status form.
    """
    class Meta:
        model = Status
        fields = ['name']
