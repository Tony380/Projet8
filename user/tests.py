from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from .forms import RegisterForm
from .views import register, LoginFormView, logout_view, profile, redirect


class TestUserUrls(TestCase):

    def test_register_url(self):
        url = reverse('user:register')
        self.assertEquals(resolve(url).func, register)

    def test_login_url(self):
        url = reverse('user:login')
        self.assertEquals(resolve(url).func.view_class, LoginFormView)

    def test_logout_url(self):
        url = reverse('user:logout')
        self.assertEquals(resolve(url).func, logout_view)

    def test_profile_url(self):
        url = reverse('user:profile')
        self.assertEquals(resolve(url).func, profile)


class TestUserViews(TestCase):

    def test_register_view(self):
        response = self.client.get(reverse('user:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_bad_register_view(self):
        response = self.client.post(reverse('user:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_login_view(self):
        response = self.client.get(reverse('user:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_logout_logged_out_view(self):
        response = self.client.get(reverse('user:logout'))
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(redirect('login.html'))

    def test_logout_logged_in_view(self):
        user = User.objects.create(username="name")
        self.client.force_login(user)
        response = self.client.get(reverse('user:logout'))
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(redirect('index.html'))

    def test_profile_logged_out_view(self):
        response = self.client.get(reverse('user:profile'))
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(redirect('login.html'))

    def test_profile_logged_in_view(self):
        user = User.objects.create(username="name")
        self.client.force_login(user)
        response = self.client.get(reverse('user:profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')


class TestUserForms(TestCase):

    def test_valid_data(self):
        form = RegisterForm(data={
            'username': 'name',
            'email': 'email@gmail.com',
            'password1': 'abdcef123',
            'password2': 'abdcef123'
        })
        self.assertTrue(form.is_valid())

    def test_no_valid_data(self):
        form = RegisterForm(data={
            'username': 'name',
            'email': 'emailgmail.com',
            'password1': 'abdcef123',
            'password2': 'abdcef123'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_no_data(self):
        form = RegisterForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)
