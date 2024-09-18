from django.db import models
from django.contrib.auth import get_user_model
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name=_('Name'),
        unique=True,
    )
    description = models.TextField(
        verbose_name=_('Description'),
        null=True,
        blank=True,
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        verbose_name=_('Status'),
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='author',
        verbose_name=_('Author'),
    )
    executor = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='executor',
        verbose_name=_('Executor'),
        null=True,
        blank=True,
    )
    label = models.ManyToManyField(
        Label,
        through='TaskToLabel',
        related_name='label',
        verbose_name=_('Label'),
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TaskToLabel(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)
