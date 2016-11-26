"""mycshub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, password_change, password_reset, password_reset_confirm
from django.conf import settings
from django.views.generic import TemplateView

from accounts.forms import RegistrationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from registration.backends.hmac.views import RegistrationView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
    url(r'^dashboard/$', TemplateView.as_view(template_name="dashboard_base.html"), name='dashboard'),
    url(r'^dashboard/messages/$', TemplateView.as_view(template_name="messages/message_list.html"), name='messages'),

    # django-registration overrides
    url(r'^accounts/register/$', RegistrationView.as_view(form_class=RegistrationForm), name='register'),
    url(r'^accounts/login/$', login, {'authentication_form':AuthenticationForm}, name='login'),
    url(r'^accounts/password/change/$', password_change,
        {'password_change_form':PasswordChangeForm,
        'post_change_redirect': 'auth_password_change_done'}, name='auth_password_change'),
    url(r'^accounts/password/reset/$', password_reset,
        {'post_reset_redirect': 'auth_password_reset_done',
         'email_template_name': 'registration/password_reset_email.txt',
         'password_reset_form':PasswordResetForm},
        name='auth_password_reset'),
    url(r'^accounts/password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/'
        r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm,
        {'post_reset_redirect': 'auth_password_reset_complete',
         'set_password_form':SetPasswordForm},
        name='auth_password_reset_confirm'),

    # django-registration urls
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^accounts/', include('registration.auth_urls')),
    url(r'^accounts/', include('accounts.urls')),

    # error urls
    url(r'^400/$', TemplateView.as_view(template_name="errors/400.html")),
    url(r'^403/$', TemplateView.as_view(template_name="errors/403.html")),
    url(r'^404/$', TemplateView.as_view(template_name="errors/404.html")),
    url(r'^500/$', TemplateView.as_view(template_name="errors/500.html")),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]


handler400 = TemplateView.as_view(template_name="errors/400.html")
handler403 = TemplateView.as_view(template_name="errors/403.html")
handler404 = TemplateView.as_view(template_name="errors/404.html")
handler500 = TemplateView.as_view(template_name="errors/500.html")
