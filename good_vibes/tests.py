from django.test import TestCase
from django.test import TestCase, SimpleTestCase
from django.urls import reverse


# Make sure we can get to home page
class MODPageTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

# TODO: We really need a test for message of the day page once we implement it
