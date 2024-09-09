from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse_lazy



class UsersTestCase(TestCase):
    CustomUser = get_user_model()
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

    def test_update(self):
        pass

    def test_delete(self):
        pass
