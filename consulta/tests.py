from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import home, lists

class TestUrls(SimpleTestCase):

    def test_home_url(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_lists_url(self):
        url = reverse('lists')
        self.assertEquals(resolve(url).func, lists)
