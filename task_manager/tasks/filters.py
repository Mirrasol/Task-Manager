from .models import Task
from task_manager.labels.models import Label
from django.utils.translation import gettext_lazy as _
from django.forms import CheckboxInput
import django_filters


class TaskFilter(django_filters.FilterSet):
    labels = django_filters.ModelChoiceFilter(queryset=Label.objects.all())
    author = django_filters.BooleanFilter(
        method='check_author',
        label=_('Personal only'),
        widget=CheckboxInput(),
    )

    class Meta:
        model = Task
        fields = ['status', 'executor']

    def check_author(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset
