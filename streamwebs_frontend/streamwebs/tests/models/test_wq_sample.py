from django.test import TestCase

from django.contrib.gis.db import models
from django.apps import apps
from itertools import chain

from streamwebs.models import WQ_Sample


class WQSampleTestCase(TestCase):

    def setUp(self):
        self.expected_fields = {
            'water_temperature': models.DecimalField,
            'water_temp_tool': models.CharField,
            'air_temperature': models.DecimalField,
            'air_temp_tool': models.CharField,
            'dissolved_oxygen': models.DecimalField,
            'oxygen_tool': models.CharField,
            'pH': models.DecimalField,
            'pH_tool': models.CharField,
            'turbidity': models.DecimalField,
            'turbid_tool': models.CharField,
            'salinity': models.DecimalField,
            'salt_tool': models.CharField,
            'conductivity': models.DecimalField,
            'total_solids': models.DecimalField,
            'bod': models.DecimalField,
            'ammonia': models.DecimalField,
            'nitrite': models.DecimalField,
            'nitrate': models.DecimalField,
            'phosphates': models.DecimalField,
            'fecal_coliform': models.DecimalField,
            'id': models.AutoField,

            # List the foreign key relation here
            'sample_1': models.ManyToOneRel,
            'sample_2': models.ManyToOneRel,
            'sample_3': models.ManyToOneRel,
            'sample_4': models.ManyToOneRel
        }

        self.optional_fields = {
            'conductivity',
            'total_solids',
            'bod',
            'ammonia',
            'nitrite',
            'nitrate',
            'phosphates',
            'fecal_coliform',
        }

    def test_fields_exist(self):
        model = apps.get_model('streamwebs', 'wq_sample')
        for field, field_type in self.expected_fields.items():
            self.assertEqual(
                field_type, type(model._meta.get_field(field)))

    def test_no_extra_fields(self):
        fields = list(set(chain.from_iterable(
            (field.name, field.attname) if hasattr(field, 'attname') else
            (field.name,) for field in WQ_Sample._meta.get_fields()
            if not (field.many_to_one and field.related_model is None)
        )))
        self.assertEqual(sorted(fields), sorted(self.expected_fields.keys()))
