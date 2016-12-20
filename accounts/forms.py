# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
)

from registration.forms import RegistrationForm

from accounts.models import UserProfile


class RegistrationForm(RegistrationForm):

    error_css_class = 'parsley-error'

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {'placeholder': 'Username', 'class': 'form-control'}
        self.fields['email'].widget.attrs = {'placeholder': 'Email', 'class': 'form-control'}
        self.fields['password1'].widget.attrs = {'placeholder': 'Password', 'class': 'form-control'}
        self.fields['password2'].widget.attrs = {'placeholder': 'Re-type Password', 'class': 'form-control'}


class AuthenticationForm(AuthenticationForm):

    error_css_class = 'parsley-error'

    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {'placeholder': 'Username', 'class': 'form-control'}
        self.fields['password'].widget.attrs = {'placeholder': 'Password', 'class': 'form-control'}


class PasswordChangeForm(PasswordChangeForm):

    error_css_class = 'parsley-error'

    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs = {'placeholder': 'Old Password', 'class': 'form-control'}
        self.fields['new_password1'].widget.attrs = {'placeholder': 'New Password', 'class': 'form-control'}
        self.fields['new_password2'].widget.attrs = {'placeholder': 'Re-type New Password', 'class': 'form-control'}


class PasswordResetForm(PasswordResetForm):

    error_css_class = 'parsley-error'

    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs = {'placeholder': 'Email Address', 'class': 'form-control'}


class SetPasswordForm(SetPasswordForm):

    error_css_class = 'parsley-error'

    def __init__(self, *args, **kwargs):
        super(SetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs = {'placeholder': 'New Password', 'class': 'form-control'}
        self.fields['new_password2'].widget.attrs = {'placeholder': 'Re-type New Password', 'class': 'form-control'}


class UserProfileEditForm(forms.ModelForm):

    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField()

    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ('user', )

    def __init__(self, instance, *args, **kwargs):
        self.user = instance.user
        super(UserProfileEditForm, self).__init__(*args, **kwargs)

        if self.user:
            self.fields['first_name'].initial = self.user.first_name
            self.fields['last_name'].initial = self.user.last_name
            self.fields['email'].initial = self.user.email

    def save(self, *args, **kwargs):
        cleaned_data = self.cleaned_data

        # save user fields
        self.user.first_name = cleaned_data['first_name']
        self.user.last_name = cleaned_data['last_name']
        self.user.email = cleaned_data['email']
        self.user.save()

        profile = self.user.profile
        profile.avatar = cleaned_data['avatar']
        profile.phone_number = cleaned_data['phone_number']
        profile.desktop_notifications = cleaned_data['desktop_notifications']
        profile.email_notifications = cleaned_data['email_notifications']
        profile.save()

        return profile
