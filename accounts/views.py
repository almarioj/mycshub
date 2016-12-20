# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.views.generic.base import View
from django.views.generic.edit import UpdateView
from django.forms import inlineformset_factory

from accounts.forms import UserProfileEditForm
from accounts.models import UserProfile
from accounts.mixins import AuthenticatedUserMixin


class DashboardIndexView(AuthenticatedUserMixin, View):
    template_name = 'dashboard_base.html'
    login_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(request, *args, **kwargs)
        return render(request, self.template_name, context)


class UserProfileView(AuthenticatedUserMixin, View):
    template_name = 'accounts/profile.html'
    login_url = reverse_lazy('login')
    form_class = UserProfileEditForm

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(request, *args, **kwargs)
        context['form'] = self.form_class(instance=request.user.profile)

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(request, *args, **kwargs)

        if 'agree_deactivate' in request.POST:
            if request.POST.get('agree_deactivate', False):
                request.user.is_active = False
                request.user.save()
                logout(request)
                messages.success(request, 'Your profile has been successfully deactivated.')
                return HttpResponseRedirect(reverse('index'))
        else:
            form = self.form_class(data=request.POST, files=request.FILES, instance=request.user.profile)
            if form.is_valid():
                form.save()
                context['form'] = self.form_class(instance=request.user.profile)
                messages.success(request, 'Profile successfully updated.')
            else:
                context['form'] = form
                messages.error(request, 'Please correct the errors below.')
            return render(request, self.template_name, context)




