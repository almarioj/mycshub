# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.views.generic import TemplateView

from accounts.views import UserProfileView, DashboardIndexView

urlpatterns = [
    url(r'^profile/$', UserProfileView.as_view(), name='profile'),
    url(r'^dashboard/$', DashboardIndexView.as_view(), name='dashboard'),
]
