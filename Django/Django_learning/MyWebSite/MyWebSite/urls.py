from django.conf.urls import patterns, include, url
from django.contrib import admin
from MyWebSite.views import *
from books import views
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MyWebSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('^$',Homepage),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^hello/$','hello'),
    url(r'^time/$',current_datetime,{'template_name': 'current_datetime.html'}),
    url(r'^another-time-page/$',current_datetime),
    url(r'^time/plus/(?P<houroffset>\d+)/$',hours_ahead),
    url(r'^broinfo/$',ua_display_good1),
    url(r'^broinfo2/$',ua_display_good2),
    url(r'^meta/$',display_meta),
    url(r'^search-form/$',views.search_form),
    url(r'^search/$',views.search),
    url(r'^contact/$',views.contact),
)

if settings.DEBUG:
    urlpatterns += patterns('',
            url(r'^hello/$',hello),
            )
