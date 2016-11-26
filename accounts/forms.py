# -*- coding: utf-8 -*-
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
)

from registration.forms import RegistrationForm

from accounts.models import UserProfile


class RegistrationForm(RegistrationForm):

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {'placeholder': 'Username', 'class': 'form-control'}
        self.fields['email'].widget.attrs = {'placeholder': 'Email', 'class': 'form-control'}
        self.fields['password1'].widget.attrs = {'placeholder': 'Password', 'class': 'form-control'}
        self.fields['password2'].widget.attrs = {'placeholder': 'Re-type Password', 'class': 'form-control'}


class AuthenticationForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {'placeholder': 'Username', 'class': 'form-control'}
        self.fields['password'].widget.attrs = {'placeholder': 'Password', 'class': 'form-control'}


class PasswordChangeForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs = {'placeholder': 'Old Password', 'class': 'form-control'}
        self.fields['new_password1'].widget.attrs = {'placeholder': 'New Password', 'class': 'form-control'}
        self.fields['new_password2'].widget.attrs = {'placeholder': 'Re-type New Password', 'class': 'form-control'}


class PasswordResetForm(PasswordResetForm):

    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs = {'placeholder': 'Email Address', 'class': 'form-control'}


class SetPasswordForm(SetPasswordForm):

    def __init__(self, *args, **kwargs):
        super(SetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs = {'placeholder': 'New Password', 'class': 'form-control'}
        self.fields['new_password2'].widget.attrs = {'placeholder': 'Re-type New Password', 'class': 'form-control'}

