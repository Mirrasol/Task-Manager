from django.forms import ModelForm
from .models import User


class UserCreateForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'password',
        ]

    def clean_username(self):
        return self.cleaned_data.get('username')
