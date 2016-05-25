from django.test import TestCase

from streamwebs.forms import UserForm, UserProfileForm
from django.contrib.gis.db import models
from django import forms
from django.apps import apps
from itertools import chain


class UserFormTestCase(TestCase):

    def setUp(self):
        self.expected_fields = ('username', 'email', 'password', 'first_name', 'last_name')

    def test_UserForm_fields_exist(self): 
        #create UserForm object
        #does it have such-and-such attribute/field????
        user_form = UserForm()
        for i in range(len(self.expected_fields)):
            self.assertEqual(user_form.Meta.fields[i], self.expected_fields[i])

class UserProfileFormTestCase(TestCase):

    def setUp(self):
        self.expected_fields = ('school', 'birthdate')

    def test_UserProfileForm_fields_exist(self):
        user_prof_form = UserProfileForm()
        for i in range(len(self.expected_fields)):
            self.assertEqual(user_prof_form.Meta.fields[i], self.expected_fields[i])
