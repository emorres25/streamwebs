from __future__ import unicode_literals

import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    SCHOOL_A = 'a'
    SCHOOL_B = 'b'
    SCHOOL_C = 'c'
    SCHOOL_CHOICES = (
      (SCHOOL_A, 'School A'),
      (SCHOOL_B, 'School B'),
      (SCHOOL_C, 'School C'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.CharField(max_length = 1, choices=SCHOOL_CHOICES, default='')
    birthdate = models.DateField(default=(datetime.date(1999, 4, 1)))
 
#    def is_valid_birthdate(self):
#        if self.birthdate.year > 2003:
#            return False

    def __unicode__(self):
        return self.user.username
