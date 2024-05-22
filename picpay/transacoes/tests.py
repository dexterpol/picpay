# transacoes/tests.py
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

class LoginTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='password123')

    def test_login_success(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'password123'})
        self.assertEqual(response.status_code, 302)  

    
       
        self.assertContains(response, 'Credenciais inválidas.')

