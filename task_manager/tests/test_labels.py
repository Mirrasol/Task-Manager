from django.test import TestCase, Client
from task_manager.labels.models import Label


class LabelsTestCase(TestCase):
    fixtures = ['labels.json']

    def setUp(self):
        self.client = Client()
        self.label1 = Label.objects.get(pk=1)
        self.label2 = Label.objects.get(pk=2)
        self.label3 = Label.objects.get(pk=3)
