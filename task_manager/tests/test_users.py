from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse_lazy


class UsersTestCase(TestCase):
    fixtures = ['labels.json', 'statuses.json', 'tasks.json', 'users.json']

    def setUp(self):
        self.client = Client()
        self.user1 = get_user_model().objects.get(pk=1)
        self.user2 = get_user_model().objects.get(pk=2)
        self.user3 = get_user_model().objects.get(pk=3)

    def test_read_unauthenticated(self):
        self.client.logout()

        response = self.client.get(reverse_lazy('users_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/index.html')

    def test_read_authenticated(self):
        self.client.force_login(self.user1)

        response = self.client.get(reverse_lazy('users_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/index.html')

    def test_create(self):
        new_user = {
            'first_name': 'Devo',
            'last_name': 'Nian',
            'username': 'Devonian',
            'password1': 40404,
            'password2': 40404,
        }

        self.client.logout()

        response = self.client.get(reverse_lazy('user_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/create.html')

        response = self.client.post(reverse_lazy('user_create'), new_user)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.get(id=4).username, 'Devonian')
        self.assertRedirects(response, reverse_lazy('login'))

    def test_update_unauthenticated(self):
        update_url = reverse_lazy('user_update', kwargs={'pk': self.user2.id})

        self.client.logout()

        response = self.client.get(update_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_update_authenticated_self(self):
        update_url = reverse_lazy('user_update', kwargs={'pk': self.user1.id})

        self.client.force_login(self.user1)

        response = self.client.get(update_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/update.html')

        updated_data = {
            'first_name': 'Cam',
            'last_name': 'Brian',
            'username': 'Cambrian_1',
            'password1': 10101,
            'password2': 10101,
        }
        response = self.client.post(update_url, updated_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.get(pk=1).username, 'Cambrian_1')
        self.assertRedirects(response, reverse_lazy('users_index'))

    def test_update_authenticated_others(self):
        update_url = reverse_lazy('user_update', kwargs={'pk': self.user3.id})

        self.client.force_login(self.user1)

        response = self.client.get(update_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('users_index'))

    def test_delete_unauthenticated(self):
        delete_url = reverse_lazy('user_delete', kwargs={'pk': self.user1.id})

        self.client.logout()

        response = self.client.get(delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_delete_authenticated_self(self):
        delete_url = reverse_lazy('user_delete', kwargs={'pk': self.user3.id})

        self.client.force_login(self.user3)

        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('users_index'))
        self.assertFalse(get_user_model().objects.contains(self.user3))

    def test_delete_authenticated_others(self):
        delete_url = reverse_lazy('user_delete', kwargs={'pk': self.user1.id})

        self.client.force_login(self.user2)

        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('users_index'))
        self.assertTrue(get_user_model().objects.contains(self.user1))

    def test_delete_linked(self):
        delete_url = reverse_lazy('user_delete', kwargs={'pk': self.user2.id})

        self.client.force_login(self.user2)

        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('users_index'))
        self.assertTrue(get_user_model().objects.contains(self.user2))
