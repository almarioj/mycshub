# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

from registration.signals import user_registered


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, related_name='profile')

    def __unicode__(self):
        return u'Profile of user: %s' % self.user.username


# signal callbacks
def user_registered_callback(sender, user, request, **kwargs):
    profile = UserProfile.objects.create(user=user)

user_registered.connect(user_registered_callback)
