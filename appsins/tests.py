from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from django.test import TestCase
from appsins.views import home_page #1
from django.http import HttpRequest

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  #2
        self.assertEqual(found.func, home_page)  #

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_catching_post_asin(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'B00000000' # 3 lines for mocking post request from user

        response = home_page(request) # invoking the view to regard our moicking request - requires additional changes in home page view

        expected_html = render_to_string(
            'home.html',
            {'new_item_text':  'B00000000'}
        )                                   ### expected_html with initiate assignment for the ASIN - only assingnment no post request
                                            ### esponse.content.decode() - actual result from view after mocking post request
        self.assertEqual(response.content.decode(), expected_html)
