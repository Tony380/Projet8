from django.test import TestCase
from django.urls import reverse, resolve
from .views import index, legal


class TestPurbeurreUrls(TestCase):

    def test_index_url(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_legal_url(self):
        url = reverse('legal')
        self.assertEquals(resolve(url).func, legal)


class TestPurbeurreViews(TestCase):

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_legal_view(self):
        response = self.client.get(reverse('legal'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'legal.html')
