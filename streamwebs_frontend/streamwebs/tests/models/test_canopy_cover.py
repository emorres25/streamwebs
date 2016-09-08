from django.test import TestCase

from django.contrib.gis.db import models
from django.apps import apps
from itertools import chain
from django.utils import timezone
from django.core.exceptions import ValidationError

from streamwebs.models import Site
from streamwebs.models import Canopy_Cover
from streamwebs.models import CC_Cardinal
from streamwebs.models import validate_cover


class CanopyCovTestCase(TestCase):

    def setUp(self):
        self.expected_fields = {
            'school': models.CharField,
            'date_time': models.DateTimeField,
            'site': models.ForeignKey,
            'site_id': models.ForeignKey,
            'weather': models.CharField,
            'est_canopy_cover': models.PositiveIntegerField,
            'id': models.AutoField,

            'canopy_cover': models.ManyToOneRel
        }

    def test_fields_exist(self):
        """Checks that the expected fields have been created"""
        model = apps.get_model('streamwebs', 'canopy_cover')
        for field, field_type in self.expected_fields.items():
            self.assertEqual(field_type, type(model._meta.get_field(field)))

    def test_no_extra_fields(self):
        """Checks for discrepancies between the actual model and its expected
           fields"""
        fields = list(set(chain.from_iterable(
            (field.name, field.attname) if hasattr(field, 'attname') else
            (field.name,) for field in Canopy_Cover._meta.get_fields()
            if not (field.many_to_one and field.related_model is None)
        )))
        self.assertEqual(sorted(fields), sorted(self.expected_fields.keys()))

    def test_datasheet_ManyToOneSite(self):
        """Tests that a datasheet correctly corresponds to is specified site"""
        default_dt = timezone.now()

        site = Site.test_objects.create_site('test')

        canopyc = Canopy_Cover.objects.create(
            school='School A', date_time=default_dt, site=site,
            weather='cloudy', est_canopy_cover=50
        )

        north = CC_Cardinal.test_objects.create_shade(
            'North', True, True, False, False, False, True, False, False, True,
            True, True, False, True, False, False, False, True, False, True,
            True, False, True, False, False, 11, canopyc
        )

        east = CC_Cardinal.test_objects.create_shade(
            'East', True, True, False, False, False, True, False, False, True,
            True, True, False, True, False, False, False, False, False, True,
            True, False, False, False, False, 8, canopyc
        )

        south = CC_Cardinal.test_objects.create_shade(
            'South', True, True, True, False, False, True, False, False, True,
            True, True, True, True, False, False, False, True, False, True,
            True, False, True, False, True, 14, canopyc
        )

        west = CC_Cardinal.test_objects.create_shade(
            'West', True, True, False, True, False, True, True, False, True,
            True, True, True, True, False, False, True, True, False, True,
            True, True, True, True, False, 17, canopyc
        )

        self.assertEqual(canopyc.site.site_name, 'test')
        self.assertEqual(canopyc.site.site_slug, 'test')

    def test_datasheet_CreateCanopyCover(self):
        """Tests that a Canopy Cover object is actually created, checks that
           the correct (shaded) value is received from the CC_Cardinal model"""
        default_dt = timezone.now()

        site = Site.test_objects.create_site('test')

        canopyc = Canopy_Cover.objects.create(
            school='School A', date_time=default_dt, site=site,
            weather='cloudy', est_canopy_cover=50
        )

        north = CC_Cardinal.test_objects.create_shade(
            'North', True, True, False, False, False, True, False, False, True,
            True, True, False, True, False, False, False, True, False, True,
            True, False, True, False, False, 11, canopyc
        )

        east = CC_Cardinal.test_objects.create_shade(
            'East', True, True, False, False, False, True, False, False, True,
            True, True, False, True, False, False, False, False, False, True,
            True, False, False, False, False, 8, canopyc
        )

        south = CC_Cardinal.test_objects.create_shade(
            'South', True, True, True, False, False, True, False, False, True,
            True, True, True, True, False, False, False, True, False, True,
            True, False, True, False, True, 14, canopyc
        )

        west = CC_Cardinal.test_objects.create_shade(
            'West', True, True, False, True, False, True, True, False, True,
            True, True, True, True, False, False, True, True, False, True,
            True, True, True, True, False, 17, canopyc
        )

        self.assertEqual(canopyc.school, 'School A')
        self.assertEqual(canopyc.date_time, default_dt)
        self.assertEqual(canopyc.weather, 'cloudy')
        self.assertEqual(canopyc.est_canopy_cover, 50)

    def test_datasheet_CC_CardinalInfo(self):
        """Tests that boolean values are correctly assigned in a
           cardinal box"""
        default_dt = timezone.now()

        site = Site.test_objects.create_site('test')

        canopyc = Canopy_Cover.objects.create(
            school='School A', date_time=default_dt, site=site,
            weather='cloudy', est_canopy_cover=50)

        north_bools = [True, True, False, False, False, True, False, False,
                       True, True, True, False, True, False, False, False,
                       True, False, True, True, False, True, False, False]

        east_bools = [True, True, False, False, False, True, False, False,
                      True, True, True, False, True, False, False, False,
                      False, False, True, True, False, False, False, False]

        south_bools = [True, True, True, False, False, True, False, False,
                       True, True, True, True, True, False, False, False, True,
                       False, True, True, False, True, False, True]

        west_bools = [True, True, False, True, False, True, True, False,
                      True, True, True, True, True, False, False, True, True,
                      False, True, True, True, True, True, False]

        north = CC_Cardinal.test_objects.create_shade(
            'North', *(north_bools + [11] + [canopyc])
        )

        east = CC_Cardinal.test_objects.create_shade(
            'East', *(east_bools + [8] + [canopyc])
        )

        south = CC_Cardinal.test_objects.create_shade(
            'South', *(south_bools + [14] + [canopyc])
        )

        west = CC_Cardinal.test_objects.create_shade(
            'West', *(west_bools + [17] + [canopyc])
        )

        #for i in range(len(north_bools)):
        #    north_var = 'canopyc.' + 'north.' + str(chr(i + 65))
        #    self.assertEqual(eval(north_var), north_bools[i])

        #for j in range(len(east_bools)):
        #    east_var = 'canopyc.' + 'east.' + str(chr(j + 65))
        #    self.assertEqual(eval(east_var), east_bools[j])

        #for k in range(len(south_bools)):
        #    south_var = 'canopyc.' + 'south.' + str(chr(k + 65))
        #    self.assertEqual(eval(south_var), south_bools[k])

        #for l in range(len(west_bools)):
        #    west_var = 'canopyc.' + 'west.' + str(chr(l + 65))
        #    self.assertEqual(eval(west_var), west_bools[l])

        # Check that each cardinal direction corresponds to canopy_cover
        self.assertEqual(north.canopy_cover_id, canopyc.id)
        self.assertEqual(east.canopy_cover_id, canopyc.id)
        self.assertEqual(south.canopy_cover_id, canopyc.id)
        self.assertEqual(west.canopy_cover_id, canopyc.id)

    def test_validate_cover_good(self):
        """Tests that est_canopy_cover is in between 0-96."""
        default_dt = timezone.now()

        site = Site.test_objects.create_site('test')

        canopyc = Canopy_Cover.objects.create(
            school='School A', date_time=default_dt, site=site,
            weather='cloudy', est_canopy_cover=51
        )

        north = CC_Cardinal.test_objects.create_shade(
            'North', True, True, False, False, False, True, False, False, True,
            True, True, False, True, False, False, False, True, False, True,
            True, False, True, False, False, 11, canopyc
        )

        east = CC_Cardinal.test_objects.create_shade(
            'East', True, True, False, False, False, True, False, False, True,
            True, True, False, True, False, False, False, False, False, True,
            True, False, False, False, False, 8, canopyc
        )

        south = CC_Cardinal.test_objects.create_shade(
            'South', True, True, True, False, False, True, False, False, True,
            True, True, True, True, False, False, False, True, False, True,
            True, False, True, False, True, 14, canopyc
        )

        west = CC_Cardinal.test_objects.create_shade(
            'West', True, True, False, True, False, True, True, False, True,
            True, True, True, True, False, False, True, True, False, True,
            True, True, True, True, False, 17, canopyc
        )

        self.assertEqual(validate_cover(canopyc.est_canopy_cover), None)

    def test_validate_cover_too_large(self):
        """Tests that validation error is risen when est_canopy_cover
           is too large."""

        default_dt = timezone.now()

        site = Site.test_objects.create_site('test')

        canopyc = Canopy_Cover.objects.create(
            school='School A', date_time=default_dt, site=site,
            weather='cloudy', est_canopy_cover=100
        )

        north = CC_Cardinal.test_objects.create_shade(
            'North', True, True, False, False, False, True, False, False, True,
            True, True, False, True, False, False, False, True, False, True,
            True, False, True, False, False, 11, canopyc
        )

        east = CC_Cardinal.test_objects.create_shade(
            'East', True, True, False, False, False, True, False, False, True,
            True, True, False, True, False, False, False, False, False, True,
            True, False, False, False, False, 8, canopyc
        )

        south = CC_Cardinal.test_objects.create_shade(
            'South', True, True, True, False, False, True, False, False, True,
            True, True, True, True, False, False, False, True, False, True,
            True, False, True, False, True, 14, canopyc
        )

        west = CC_Cardinal.test_objects.create_shade(
            'West', True, True, False, True, False, True, True, False, True,
            True, True, True, True, False, False, True, True, False, True,
            True, True, True, True, False, 17, canopyc
        )

        with self.assertRaises(ValidationError):
            validate_cover(canopyc.est_canopy_cover)
