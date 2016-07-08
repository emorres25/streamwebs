from django.test import TestCase
from django.contrib.gis.db import models
from django.apps import apps
from itertools import chain
from streamwebs.models import PhotoPoint


class PhotoPointTestCase(TestCase):

    def setUp(self):
        self.expected_fields = {
            'camera_point': models.ForeignKey,
            'pp_date': models.DateField,
            'compass_bearing': models.DecimalField,
            'distance_feet': models.PositiveSmallIntegerField,
            'distance_inches': models.PositiveSmallIntegerField,
            'camera_height_feet': models.PositiveSmallIntegerField,
            'camera_height_inches': models.PositiveSmallIntegerField,
            'photo_filename': models.CharField,
            'photo': models.ImageField,
            'notes': models.TextField,
            'id': models.AutoField,

            'camera_point_id': models.ForeignKey
        }

        self.optional_fields = {
            'distance_feet': models.PositiveSmallIntegerField,
            'distance_inches': models.PositiveSmallIntegerField,
            'camera_height_feet': models.PositiveSmallIntegerField,
            'camera_height_inches': models.PositiveSmallIntegerField,
            'photo_filename': models.CharField,
            'photo': models.ImageField,
            'notes': models.TextField
        }


    def test_fields_exist(self):
        """
        The model's field types and the expected field types listed in setUp
        should match exactly.
        """
        pp_model = apps.get_model('streamwebs', 'photopoint')
        for field, field_type in self.expected_fields.items():
            self.assertEqual(field_type, type(pp_model._meta.get_field(field)))

    def test_no_extra_fields(self):
        """
        The model's field names and the expected field names listed in setUp
        should match exactly.
        """
        # MyModel._meta.get_all_field_names() is deprecated. The following is
        # an alternative, as suggested by the Django docs:
        # https://docs.djangoproject.com/en/1.9/ref/models/meta/
        pp_fields = list(set(chain.from_iterable(
            (field.name, field.attname) if hasattr(field, 'attname') else
            (field.name,) for field in PhotoPoint._meta.get_fields()
            if not (field.many_to_one and field.related_model is None)
            )))
        self.assertEqual(sorted(pp_fields),
                         sorted(self.expected_fields.keys()))

    def test_optional_fields(self):
        apps.get_model('streamwebs', 'photopoint')
        for field in self.optional_fields:
            self.assertEqual(
                PhotoPoint._meta.get_field(field).blank, True)
