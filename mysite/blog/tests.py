from django.test import TestCase
from django.urls import reverse
from models import Post

# Create your tests here.
class BlogTests(TestCase):
    def setUp(self):
        # Setup run before every test method.
        pass

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_health_check(self):
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)

