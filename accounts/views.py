# -*- coding: utf-8 -*-
from django.views.generic.base import View
from django.shortcuts import render

from accounts.models import UserProfile


class UserProfileView(View):

    template_name = 'accounts/profile.html'

    def get(self, request, *args, **kwargs):
        profile = UserProfile.objects.get(user=request.user)
        return render(request, self.template_name, {'profile':profile})

