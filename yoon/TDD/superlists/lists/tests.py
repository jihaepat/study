from django.urls import reverse
from django.test import TestCase

class SmokeTest(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1+1,3)

# class HomePageTest(TestCase):
#
#     def test_root_url_resolves_to_page_view(self):
#         found = reverse('/')
#         self.assertEqual(found.func, home_page)

