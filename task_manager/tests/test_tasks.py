from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from task_manager.tasks.models import Task
from django.urls import reverse_lazy


class TaskTestCase(TestCase):
    fixtures = ['labels.json', 'statuses.json', 'tasks.json', 'users.json']

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.get(pk=1)
        self.task1 = Task.objects.get(pk=1)
        self.task2 = Task.objects.get(pk=2)
        self.task3 = Task.objects.get(pk=3)

    def test_read_index_unauthenticated(self):
        self.client.logout()

        response = self.client.get(reverse_lazy('tasks_index'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_read_index_authenticated(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse_lazy('tasks_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/index.html')

    def test_read_task_unauthenticated(self):
        task_url = reverse_lazy('task_overview', kwargs={'pk': self.task1.id})

        self.client.logout()

        response = self.client.get(task_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_read_task_authenticated(self):
        task_url = reverse_lazy('task_overview', kwargs={'pk': self.task2.id})

        self.client.force_login(self.user)

        response = self.client.get(task_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/overview.html')

    def test_create_unauthenticated(self):
        self.client.logout()

        response = self.client.get(reverse_lazy('task_create'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_create_authenticated(self):
        new_task = {
            'name': 'Project D',
            'description': 'Whatsoever',
            'author': '1',
            'executor': '2',
            'status': '1',
            'created_at': '2024-09-15 00:03:35.000001+03',
        }

        self.client.force_login(self.user)

        response = self.client.get(reverse_lazy('task_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/create.html')

        response = self.client.post(reverse_lazy('task_create'), new_task)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.get(id=4).name, 'Project D')
        self.assertRedirects(response, reverse_lazy('tasks_index'))

    def test_update_unauthenticated(self):
        update_url = reverse_lazy('task_update', kwargs={'pk': self.task1.id})

        self.client.logout()

        response = self.client.get(update_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_update_authenticated(self):
        update_url = reverse_lazy('task_update', kwargs={'pk': self.task3.id})

        self.client.force_login(self.user)

        response = self.client.get(update_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/update.html')

        updated_data = {
            'name': 'Project C',
            'description': 'Update imminent',
            'executor': '2',
            'status': '1',
        }

        response = self.client.post(update_url, updated_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.get(pk=3).description, 'Update imminent')
        self.assertRedirects(response, reverse_lazy('tasks_index'))

    def test_delete_unauthenticated(self):
        delete_url = reverse_lazy('task_delete', kwargs={'pk': self.task3.id})

        self.client.logout()

        response = self.client.get(delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_delete_authenticated_author(self):
        delete_url = reverse_lazy('task_delete', kwargs={'pk': self.task3.id})

        self.client.force_login(self.user)

        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('tasks_index'))
        self.assertFalse(Task.objects.contains(self.task3))

    def test_delete_authenticated_not_author(self):
        delete_url = reverse_lazy('task_delete', kwargs={'pk': self.task2.id})

        self.client.force_login(self.user)

        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('tasks_index'))
        self.assertTrue(Task.objects.contains(self.task2))

    def test_filter_by_status(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse_lazy('tasks_index'), {'status': 2})
        self.assertEqual(response.context['tasks'].count(), 2)
        response = self.client.get(reverse_lazy('tasks_index'), {'status': 3})
        self.assertEqual(response.context['tasks'].count(), 0)

    def test_filter_by_executor(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse_lazy('tasks_index'), {'executor': 1})
        self.assertEqual(response.context['tasks'].count(), 1)
        response = self.client.get(reverse_lazy('tasks_index'), {'executor': 3})
        self.assertEqual(response.context['tasks'].count(), 0)

    def test_filter_by_labels(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse_lazy('tasks_index'), {'label': 1})
        self.assertEqual(response.context['tasks'].count(), 1)
        response = self.client.get(reverse_lazy('tasks_index'), {'label': 3})
        self.assertEqual(response.context['tasks'].count(), 0)

    def test_filter_personal_tasks(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse_lazy('tasks_index'), {'author': True})
        self.assertEqual(response.context['tasks'].count(), 2)
        self.assertTrue(response.context['tasks'].contains(self.task1))
        self.assertFalse(response.context['tasks'].contains(self.task2))
