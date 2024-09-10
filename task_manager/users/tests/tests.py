from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse_lazy


class UsersTestCase(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.client = Client()
        self.user1 = get_user_model().objects.get(pk=1)
        self.user2 = get_user_model().objects.get(pk=2)
        self.user3 = get_user_model().objects.get(pk=3)

    def test_create(self):
        new_user = {
            'first_name': 'Devo',
            'last_name': 'Nian',
            'username': 'Devonian',
            'password1': 40404,
            'password2': 40404,
        }

        response = self.client.get(reverse_lazy('create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/create.html')

        response = self.client.post(reverse_lazy('create'), new_user)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.get(id=4).username, 'Devonian')
        self.assertRedirects(response, reverse_lazy('login'))

    def test_update_unauthenticated(self):
        update_url = reverse_lazy('update', kwargs={'pk': self.user2.id})

        response = self.client.get(update_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_update_authenticated_self(self):
        self.client.force_login(self.user1)
        update_url = reverse_lazy('update', kwargs={'pk': self.user1.id})

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
        self.assertEqual(get_user_model().objects.get(id=1).username, 'Cambrian_1')
        self.assertRedirects(response, reverse_lazy('users_index'))

    def test_update_authenticated_others(self):
        self.client.force_login(self.user1)
        update_url = reverse_lazy('update', kwargs={'pk': self.user3.id})

        response = self.client.get(update_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('users_index'))

    def test_delete_unauthenticated(self):
        self.client.logout()
        delete_url = reverse_lazy('delete', kwargs={'pk': self.user1.id})

        response = self.client.get(delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_delete_authenticated_self(self):
        self.client.force_login(self.user1)
        delete_url = reverse_lazy('delete', kwargs={'pk': self.user1.id})

        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))
        self.assertFalse(self.user1.exists())

    def test_delete_authenticated_others(self):
        self.client.force_login(self.user2)
        delete_url = reverse_lazy('delete', kwargs={'pk': self.user3.id})

        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('users_index'))
        self.assertTrue(self.user3.exists())
