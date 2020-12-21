from django.test import SimpleTestCase
from django.urls import resolve,reverse
from sweet_fac.views import home,Add,see
class Testurls(SimpleTestCase):
    def test_url_resolve_home(self):
        url=reverse('home')
        self.assertEquals(resolve(url).func,home)
    
    def test_url_resolve_Add(self):
        url=reverse('Add')
        self.assertEquals(resolve(url).func,Add)
    
    def test_url_resolve_see(self):
        url=reverse('see')
        self.assertEquals(resolve(url).func,see)