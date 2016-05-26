from django.test import Client, TestCase
from django.core.urlresolvers import reverse

from streamwebs.forms import UserForm, UserProfileForm


class RegistrateTestCase(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_view_with_registered_user(self):
        """
        When the user has been registered, they should see a "thanks for registering" page
        """
        self.registered = False
        response = self.client.get(reverse('streamwebs:register'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You have successfully created a StreamWebs account.")
    
