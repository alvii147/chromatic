from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_GET(self):
        url = reverse('chromatic_app_home')
        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'chromatic_app/home.html')

    def test_login_GET(self):
        url = reverse('chromatic_app_login')
        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'chromatic_app/login.html')

    def test_register_GET(self):
        url = reverse('chromatic_app_register')
        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'chromatic_app/register.html')