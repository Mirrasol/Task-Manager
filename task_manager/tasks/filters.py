from .models import Task
from django.utils.translation import gettext_lazy as _
import django_filters


class TaskFilter(django_filters.FilterSet):
    personal_tasks = django_filters.BooleanFilter(
        field_name='author',
        label=_('Personal only'),
        widget=django_filters.widgets.BooleanWidget(),
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']
