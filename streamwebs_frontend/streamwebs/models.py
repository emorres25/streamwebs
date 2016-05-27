from __future__ import unicode_literals

import datetime

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from django.conf import settings

# Create your models here.

def validate_UserProfile_school(school):
    if not school in dict(settings.SCHOOL_CHOICES):
        raise ValidationError('That school is not in the list.')

def validate_UserProfile_birthdate(birthdate):
    today = datetime.datetime.now() 
    if birthdate.year > today.year - 13:
        raise ValidationError('You must have been born before %s' % (today.year-13))
    elif birthdate.year == today.year - 13:
        if birthdate.month > today.month: 
            raise ValidationError('You are not yet 13 (month)')
        elif birthdate.month == today.month:
            if birthdate.day > today.day:
                raise ValidationError('You are not yet 13 (days)')
            
class UserProfile(models.Model):
#    SCHOOL_A = 'a'
#    SCHOOL_B = 'b'
#    SCHOOL_C = 'c'
#    SCHOOL_CHOICES = (
#      (SCHOOL_A, 'School A'),
#      (SCHOOL_B, 'School B'),
#      (SCHOOL_C, 'School C'),
#    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.CharField(max_length = 1, choices=settings.SCHOOL_CHOICES, default='', validators=[validate_UserProfile_school])
    birthdate = models.DateField(validators=[validate_UserProfile_birthdate])

    def __unicode__(self):
        return self.user.username
