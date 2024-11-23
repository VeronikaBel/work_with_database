from django.test import TestCase
from django.urls import reverse

class CatalogTest(TestCase):
    
    def test_catalog_page_status_code(self):
        response = self.client.get(reverse('phones:catalog'))
        self.assertEqual(response.status_code, 200)