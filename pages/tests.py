from pages.views import HomePageView
from django.test import SimpleTestCase
from django.urls import reverse,resolve
from django.views.generic.base import View

from .views import HomePageView


# Create your tests here.
class Homepagetests(SimpleTestCase):

    def setUp(self):
        url=reverse('home')
        self.response=self.client.get(url)



    def test_homepage_status_code(self):  
        self.assertEqual(self.response.status_code,200)
    
    def test_homepage_template_test(self):
        self.assertTemplateUsed(self.response,'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response,'Homepage')

    def test_Homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response,"i am not here")

    def test_homepage_url_resolves_homepageView(self):
        view=resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
