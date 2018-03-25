from django.http import HttpRequest
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import resolve
from django.test import TestCase
from .views import home_page
from .models import Item
import re

# Create your tests here.
#
# class SmokeTest(TestCase):
#     def test_bad_maths(self):
#         self.assertEqual(1 + 1, 3)

class HomePageTest(TestCase):

    pattern_input_csrf = re.compile(r'<input[^>]*csrfmiddlewaretoken[^>]*>')

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        # self.assertTrue(response.content.startswith(b'<html>'))
        # self.assertIn(b'<title>To-Do lists</title>', response.content)
        # self.assertTrue(response.content.endswith(b'</html>'))

        expected_html = render_to_string('home.html')

        self.assertEqual(
            re.sub(self.pattern_input_csrf, '', response.content.decode()),
            re.sub(self.pattern_input_csrf, '', expected_html),
        )

    def test_home_page_can_save_a_POST_request(self):

        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = '신규 작업 아이템'

        response = home_page(request)

        self.assertIn('신규 작업 아이템', response.content.decode())
        expected_html = render_to_string(
            'home.html',
            {'new_item_text': '신규 작업 아이템'},
        )
        self.assertEqual(
            re.sub(self.pattern_input_csrf, '', response.content.decode()),
            re.sub(self.pattern_input_csrf, '', expected_html),
        )

class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = '첫 번째 아이템'
        first_item.save()

        second_item = Item()
        second_item.text = '두 번째 아이템'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(),2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item, '첫 번째 아이템')
        self.assertEqual(second_item, '두 번째 아이템')