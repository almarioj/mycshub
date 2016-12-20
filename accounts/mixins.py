# -*- coding: utf-8 -*-
from django.http import Http404

from braces.views import LoginRequiredMixin

from accounts.models import UserProfile


class AuthenticatedUserMixin(LoginRequiredMixin):

    def get_context_data(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            raise Http404

        try:
            context = {}
            context['profile'] = request.user.profile
        except UserProfile.DoesNotExist:
            raise Http404
        return context
