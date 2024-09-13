from django.test import TestCase, Client
from .models import Status


class StatusesTestCase(TestCase):
    fixtures = ['statuses.json']

    def setUp(self):
        self.client = Client()
        self.status1 = Status.objects.get(pk=1)
        self.status2 = Status.objects.get(pk=2)
        self.status3 = Status.objects.get(pk=3)
