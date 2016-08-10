from django.test import TestCase
from streamwebs.models import School
from django.contrib.gis.db import models
from django.apps import apps
from itertools import chain


class SchoolTestCase(TestCase):

    def setUp(self):
        self.expected_fields = {
            'name': models.CharField,
            'school_type': models.CharField,
            'address': models.CharField,
            'city': models.CharField,
            'zipcode': models.CharField,

            'created': models.DateTimeField,
            'modified': models.DateTimeField,

            'id': models.AutoField,
        }

    def test_fields_exist(self):
        model = apps.get_model('streamwebs', 'school')
        for field, field_type in self.expected_fields.items():
            self.assertEqual(
                field_type, type(model._meta.get_field(field)))

    def test_no_extra_fields(self):
        # the following is equivalent to MyField._meta.get_all_field_names()
        # which was deprecated in Django 1.9
        fields = list(set(chain.from_iterable(
            (field.name, field.attname) if hasattr(field, 'attname') else
            (field.name,) for field in School._meta.get_fields()
            if not (field.many_to_one and field.related_model is None)
        )))
        self.assertEqual(sorted(fields), sorted(self.expected_fields.keys()))

    def test_create_and_mod_dates(self):
        """When a new school is created, both date fields should be set"""
        self.assertTrue(School._meta.get_field('modified').auto_now)
        self.assertTrue(School._meta.get_field('created').auto_now_add)
