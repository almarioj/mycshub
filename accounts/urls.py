# -*- coding: utf-8 -*-
from django.conf.urls import url, include

from accounts.views import UserProfileView

urlpatterns = [
    url(r'^profile/$', UserProfileView.as_view(), name='profile')
]
