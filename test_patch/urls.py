from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from test_patch.app.resources import TestResource

test_resource = TestResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project_name.views.home', name='home'),
    # url(r'^project_name/', include('project_name.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url('^$', TemplateView.as_view(
        template_name='home.html'
        )),
    url(r'^api/', include(test_resource.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
