from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse_lazy

CustomUser = get_user_model()


class UsersTestCase(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.client = Client()
        self.user1 = CustomUser.objects.get(pk=1)
        self.user2 = CustomUser.objects.get(pk=2)
        self.user3 = CustomUser.objects.get(pk=3)

    def test_create(self):
        new_user = {
            'first_name': 'Devo',
            'last_name': 'Nian',
            'username': 'Devonian',
            'password1': 40404,
            'password2': 40404,
        }
        create_url = reverse_lazy('create')

        response = self.client.get(create_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/create.html')

        response = self.client.post(create_url, new_user)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(CustomUser.objects.get(id=4).username, 'Devonian')
        self.assertRedirects(response, reverse_lazy('login'))

    def test_update_unauthenticated(self):
        update_url = reverse_lazy('update', kwargs={'pk': self.user2.id})

        response = self.client.get(update_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_update_authenticated_self(self):
        self.client.force_login(self.user1)
        update_url = reverse_lazy('update', kwargs={'pk': self.user1.id})
        index_url = reverse_lazy('users_index')

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
        self.assertEqual(CustomUser.objects.get(id=1).username, 'Cambrian_1')
        self.assertRedirects(response, index_url)

    def test_update_authenticated_others(self):
        self.client.force_login(self.user1)
        update_url = reverse_lazy('update', kwargs={'pk': self.user3.id})
        index_url = reverse_lazy('users_index')

        response = self.client.get(update_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, index_url)

    def test_delete(self):
        pass
