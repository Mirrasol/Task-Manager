from django.forms import ModelForm
from .models import Label


class LabelForm(ModelForm):
    """
    A custom Label form.
    """
    class Meta:
        model = Label
        fields = ['name']
