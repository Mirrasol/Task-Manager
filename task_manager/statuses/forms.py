from django.forms import ModelForm
from .models import Status


class StatusCreateForm(ModelForm):
    class Meta:
        model = Status
        fields = ['name']
