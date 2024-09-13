from django.forms import ModelForm
from .models import Label


class LabelCreateForm(ModelForm):
    class Meta:
        model = Label
        fields = ['name']
