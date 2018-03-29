from django.http import HttpRequest
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import resolve
from django.test import TestCase
from .views import home_page
from .models import Item, List
import re


class HomePageTest(TestCase):
    pattern_input_csrf = re.compile(r'<input[^>]*csrfmiddlewaretoken[^>]*>')

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)

        expected_html = render_to_string('home.html')

        self.assertEqual(
            re.sub(self.pattern_input_csrf, '', response.content.decode()),
            re.sub(self.pattern_input_csrf, '', expected_html),
        )

    # def test_home_page_only_saves_items_when_necessary(self):
    #     request = HttpRequest()
    #     home_page(request)
    #     self.assertEqual(Item.objects.count(), 0)


class ListViewTest(TestCase):

    def test_uses_list_template(self):
        list = List.objects.create()
        # response = self.client.get('/lists/the-only-list-in-the-world/')
        # print('456456456', list.id, '--------------------')
        response = self.client.get('/lists/%d/' % (list.id,))
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_only_items_for_that_list(self):
        correct_list = List.objects.create()

        Item.objects.create(text='itemey 1', list=correct_list)
        Item.objects.create(text='itemey 2', list=correct_list)

        other_list = List.objects.create()

        print('55555555555  ',other_list)
        Item.objects.create(text='다른 목록 아이템 1', list=other_list)
        Item.objects.create(text='다른 목록 아이템 2', list=other_list)

        print('123132132  ',correct_list.id, '-------------------')
        response = self.client.get('/lists/%d' % (correct_list.id,))
        print(response)

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
        self.assertNotContains(response, '다른 목록 아이템 1')
        self.assertNotContains(response, '다른 목록 아이템 2')
        # response = self.client.get('/lists/1/')
        # print(response)
        #
        # self.assertContains(response, 'itemey 1')
        # self.assertContains(response, 'itemey 2')


class NewListTest(TestCase):

    def test_saving_a_POST_request(self):
        # request = HttpRequest()
        # request.method = 'POST'
        # request.POST['item_text'] = 'A new list item'
        #
        # response = home_page(request)
        #
        # self.assertEqual(Item.objects.count(), 1)
        # new_item = Item.objects.first()
        # self.assertEqual(new_item.text, 'A new list item')
        self.client.post(
            '/lists/new',
            data={'item_text': '신규 작업 아이템'}
        )
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, '신규 작업 아이템')

    def test_redirect_after_POST(self):
        # request = HttpRequest()
        # request.method = 'POST'
        # request.POST['item_text'] = 'A new list item'
        #
        # response = home_page(request)
        #

        respone = self.client.post(
            '/lists/new',
            data={'item_text': '신규 작업 아이템'}
        )
        # self.assertEqual(respone.status_code, 302)
        new_list = List.objects.first()
        self.assertRedirects(respone, '/lists/%d/' % (new_list.id,))


class NewItemTest(TestCase):
    def test_can_save_a_POST_request_to_an_existing_list(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        self.client.post(
            '/lists/%d/add_item' % (correct_list.id,),
            data = {'item_text' : '기존 목록에 신규 아이템'}
        )
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, '기존 목록에 신규 아이템')
        self.assertEqual(new_item.list, correct_list)
    def test_redirects_to_list_view(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        response = self.client.post(
            '/lists/%d/add_item' %(correct_list.id),
            data={'item_text': '기존 목록에 신규 아이템'}
        )

        self.assertRedirects(response, '/lists/%d/'%(correct_list.id,))

class ListandItemModelstest(TestCase):

    def test_saving_and_retrieving_items(self):
        list = List()
        list.save()

        first_item = Item()
        first_item.text = '첫 번째 아이템'
        first_item.list = list
        first_item.save()

        second_item = Item()
        second_item.text = '두 번째 아이템'
        second_item.list = list
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, '첫 번째 아이템')
        # print(first_saved_item.list,'--------------',list)
        self.assertEqual(first_saved_item.list, list)
        self.assertEqual(second_saved_item.text, '두 번째 아이템')
        self.assertEqual(second_saved_item.list, list)
