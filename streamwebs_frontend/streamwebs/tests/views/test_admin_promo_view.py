from django.test import Client, TestCase
from django.core.urlresolvers import reverse
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User, Group, Permission


class AdminPromoTestCase(TestCase):
    fixtures = ['sample_users.json']

    def setUp(self):
        self.client = Client()
        admins = Group.objects.get(name='admin')
        can_promo = Permission.objects.get(codename='can_promote_users')

        self.user1 = User.objects.get(pk=2)
        self.user2 = User.objects.get(pk=7)

        # super admin (level: Renee) with promotion permission
        self.superAdmin = User.objects.create_user('superAdmin',
                                                   'super@example.com',
                                                   'superpassword')
        self.superAdmin.groups.add(admins)
        self.superAdmin.user_permissions.add(can_promo)

        # regular admin (level: Renee's colleague) without promotion permission
        self.regAdmin = User.objects.create_user('regAdmin', 'reg@example.com',
                                                 'regpassword')
        self.regAdmin.groups.add(admins)

    def test_data_loaded_and_usable(self):
        """Check users exist in test db and that admins have correct perms"""
        self.assertEquals(User.objects.count(), 9)
        self.assertTrue(self.superAdmin.has_perms(
            ['streamwebs.can_view_stats', 'streamwebs.can_upload_resources',
             'streamwebs.can_promote_users']))
        self.assertTrue(self.regAdmin.has_perms(
            ['streamwebs.can_view_stats', 'streamwebs.can_upload_resources']))
        self.assertFalse(self.regAdmin.has_perm(
            'streamwebs.can_promote_users'))
        self.assertTrue(self.regAdmin.groups.filter(name='admin').exists())
        self.assertTrue(self.superAdmin.groups.filter(name='admin').exists())

    def test_not_logged_in_user(self):
        """If user not logged in, can't view page, period."""
        response = self.client.get(reverse('streamwebs:user_promo'))

        self.assertRedirects(
            response,
            (reverse('streamwebs:login') + '?next=' +
                reverse('streamwebs:user_promo')),
            status_code=302,
            target_status_code=200)
        self.assertTemplateNotUsed(
            response, 'streamwebs/admin/user_promo.html')

    def test_superAdmin_can_view(self):
        """Admin with promo perm should be able to view the page"""
        self.client.login(username='superAdmin', password='superpassword')
        response = self.client.get(reverse('streamwebs:user_promo'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'streamwebs/admin/user_promo.html')

        self.client.logout()

    def test_regAdmin_cannot_view(self):
        """Admin w/o promo perm should be denied access to the page"""
        self.client.login(username='regAdmin', password='regpassword')
        response = self.client.get(reverse('streamwebs:user_promo'))

        self.assertRaises(PermissionDenied)
        self.assertEquals(response.status_code, 403)
        self.assertTemplateNotUsed(response,
                                   'streamwebs/admin/user_promo.html')
        self.client.logout()

    def test_view_with_bad_blank_data(self):
        """If user submits bad (blank) form, form errors displayed"""
        self.client.login(username='superAdmin', password='superpassword')
        response = self.client.post(reverse('streamwebs:user_promo'), {})
        self.assertFormError(response, 'promo_form', 'users',
                             'This field is required.')
        self.assertFormError(response, 'promo_form', 'perms',
                             'This field is required.')
        self.client.logout()

    def test_add_users_to_admin_group(self):
        """Tests that users can be added to the admin group"""
        self.client.login(username='superAdmin', password='superpassword')

        self.assertFalse(self.user1.groups.filter(name='admin').exists())
        self.assertFalse(self.user2.groups.filter(name='admin').exists())

        response = self.client.post(reverse('streamwebs:user_promo'), {
            'users': (self.user1.id, self.user2.id),
            'perms': 'add_admin',
            }
        )
        self.assertTrue(self.user1.groups.filter(name='admin').exists())
        self.assertTrue(self.user2.groups.filter(name='admin').exists())

    def test_remove_users_from_admin_group(self):
        """Tests that users can be removed from the admin group"""
        self.client.login(username='superAdmin', password='superpassword')

        response = self.client.post(reverse('streamwebs:user_promo'), {
            'users': (self.user1.id),
            'perms': 'del_admin',
            }
        )
        self.assertFalse(self.user1.groups.filter(name='admin').exists())

    def test_add_stats_perm_for_users(self):
        """Tests that users can be granted the can_view_stats permission"""
        self.client.login(username='superAdmin', password='superpassword')

        response = self.client.post(reverse('streamwebs:user_promo'), {
            'users': (self.user1.id),
            'perms': 'add_stats',
            }
        )
        self.assertTrue(self.user1.has_perm('streamwebs.can_view_stats'))

    def test_remove_stats_perm_for_users(self):
        """Tests that users can have the can_view_stats permission revoked"""
        self.client.login(username='superAdmin', password='superpassword')

        response = self.client.post(reverse('streamwebs:user_promo'), {
            'users': (self.user1.id, self.user2.id),
            'perms': 'del_stats',
            }
        )
        self.assertFalse(self.user1.has_perm('streamwebs.can_view_stats'))
        self.assertFalse(self.user2.has_perm('streamwebs.can_view_stats'))

    def test_add_upload_perm_for_users(self):
        """Tests that users can be granted the can_upload_resources perm"""
        self.client.login(username='superAdmin', password='superpassword')

        response = self.client.post(reverse('streamwebs:user_promo'), {
            'users': (self.user1.id),
            'perms': 'add_upload',
            }
        )
        self.assertTrue(self.user1.has_perm('streamwebs.can_upload_resources'))

    def test_remove_upload_perm_for_users(self):
        """Tests that users can have the can_upload_stats permission revoked"""
        self.client.login(username='superAdmin', password='superpassword')

        response = self.client.post(reverse('streamwebs:user_promo'), {
            'users': (self.user1.id, self.user2.id),
            'perms': 'del_upload',
            }
        )
        self.assertFalse(self.user1.has_perm(
            'streamwebs.can_upload_resources'))
        self.assertFalse(self.user2.has_perm(
            'streamwebs.can_upload_resources'))
