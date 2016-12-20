# -*- coding: utf-8 -*-
import os

from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

from easy_thumbnails.signals import saved_file
from easy_thumbnails.signal_handlers import generate_aliases_global

from registration.signals import user_registered


def get_upload_dir(instance, filename):
    if isinstance(instance, UserProfile):
        extension = filename.split('.')[-1]
        filename = u'{}.{}'.format(instance.id, extension)
        return os.path.join('avatar', filename)
    return filename


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, related_name='profile')
    avatar = models.ImageField('profile picture', upload_to=get_upload_dir, null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(max_length=16, validators=[phone_regex], blank=True, null=True)

    desktop_notifications = models.BooleanField(default=False)
    email_notifications = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def __unicode__(self):
        return u'Profile of user: %s' % self.user.username

    @property
    def get_display_name(self):
        return self.user.get_full_name() or self.user.username


# signals
def user_registered_callback(sender, user, request, **kwargs):
   profile = UserProfile.objects.create(user=user)
   return profile

user_registered.connect(user_registered_callback)
saved_file.connect(generate_aliases_global)

