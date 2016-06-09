from django.test import Client, TestCase
from django.core.urlresolvers import reverse


class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_not_logged_in_view(self):
        """
        When the user hasn't logged in yet, they should see a "Log In" message
        """
        response = self.client.get(reverse('streamwebs:login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Log In')
