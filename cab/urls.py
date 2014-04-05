from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cab.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^homepage/$','webpage.views.homepage'),
    url(r'^bookpage/$','webpage.views.bookpage'),
    url(r'^statuspage/$','webpage.views.statuspage'),
    url(r'^book_1/$','webpage.views.book_1'),
    url(r'^book_adv/$','webpage.views.book_adv'),
    url(r'^save_adv/$','webpage.views.save_adv'),
    url(r'^signup/$','webpage.views.signup'),
    url(r'login/$','webpage.views.login'),
    url(r'^admin/', include(admin.site.urls)),


)
