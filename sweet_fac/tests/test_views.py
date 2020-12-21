from django.urls import reverse
from sweet_fac.models import models
import json
from django.test import TestCase,Client
class Testview(TestCase):
    def test_home_get(self):
        
        self.response=self.client.get(reverse('home'))
        self.assertTemplateUsed(self.response,"home.html")
    def test_see_get(self):
        
        self.response=self.client.get(reverse('see'))
        self.assertTemplateUsed(self.response,"see.html")
    def test_Add_get(self):
        
        self.response=self.client.get(reverse('Add'))
        self.assertTemplateUsed(self.response,"Add.html")