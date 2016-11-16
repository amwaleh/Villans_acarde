from django.test import TestCase, Client
from django.core.urlresolvers import reverse


class TestViews(TestCase):
    def setUp(self):
        client = Client()


    def test_landing_page(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertContains(response,"home")
