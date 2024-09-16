from django.test import TestCase, Client
from task_manager.tasks.models import Task


class LabelsTestCase(TestCase):
    fixtures = ['labels.json', 'statuses.json', 'tasks.json', 'users.json']

    def setUp(self):
        self.client = Client()
        self.task1 = Task.objects.get(pk=1)
        self.task2 = Task.objects.get(pk=2)
        self.task3 = Task.objects.get(pk=3)
