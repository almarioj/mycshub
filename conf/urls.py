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
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
    url(r'^login/$', TemplateView.as_view(template_name="auth/login.html"), name='login'),
    url(r'^dashboard/$', TemplateView.as_view(template_name="dashboard_base.html"), name='dashboard'),
    url(r'^dashboard/messages/$', TemplateView.as_view(template_name="messages/message_list.html"), name='messages'),

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
