from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from task_manager.labels.models import Label
from django.urls import reverse_lazy


class LabelsTestCase(TestCase):
    fixtures = ['labels.json', 'statuses.json', 'tasks.json', 'users.json']

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.get(pk=1)
        self.label1 = Label.objects.get(pk=1)
        self.label2 = Label.objects.get(pk=2)
        self.label3 = Label.objects.get(pk=3)

    def test_read_unauthenticated(self):
        self.client.logout()

        response = self.client.get(reverse_lazy('labels_index'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_read_authenticated(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse_lazy('labels_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/index.html')

    def test_create_unauthenticated(self):
        self.client.logout()

        response = self.client.get(reverse_lazy('label_create'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_create_authenticated(self):
        new_label = {
            'name': 'testing',
            'created_at': '2024-09-13 00:04:04.000001+03'
        }

        self.client.force_login(self.user)

        response = self.client.get(reverse_lazy('label_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/create.html')

        response = self.client.post(reverse_lazy('label_create'), new_label)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Label.objects.get(id=4).name, 'testing')
        self.assertRedirects(response, reverse_lazy('labels_index'))

    def test_update_unauthenticated(self):
        update_url = reverse_lazy('label_update', kwargs={'pk': self.label1.id})

        self.client.logout()

        response = self.client.get(update_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_update_authenticated(self):
        update_url = reverse_lazy('label_update', kwargs={'pk': self.label1.id})

        self.client.force_login(self.user)

        response = self.client.get(update_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/update.html')

        updated_data = {
            'name': 'updated',
        }

        response = self.client.post(update_url, updated_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Label.objects.get(pk=1).name, 'updated')
        self.assertRedirects(response, reverse_lazy('labels_index'))

    def test_delete_unauthenticated(self):
        delete_url = reverse_lazy('label_delete', kwargs={'pk': self.label3.id})

        self.client.logout()

        response = self.client.get(delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_delete_authenticated(self):
        delete_url = reverse_lazy('label_delete', kwargs={'pk': self.label3.id})

        self.client.force_login(self.user)

        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('labels_index'))
        self.assertFalse(Label.objects.contains(self.label3))

    def test_delete_linked(self):
        delete_url = reverse_lazy('label_delete', kwargs={'pk': self.label2.id})

        self.client.force_login(self.user)

        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('labels_index'))
        self.assertTrue(Label.objects.contains(self.label2))
