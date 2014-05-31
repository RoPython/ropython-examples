from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from jukebox.tracks.views import ArtistList, Playlist
from jukebox.auth.views import AuthCreate, AuthTokenList

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jukebox.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^playlist/$', Playlist.as_view(), name='tracks'),
    url(r'^artists/$', ArtistList.as_view(), name='artists'),
    url(r'^auth/$', AuthCreate.as_view(), name='auth'),
    url(r'^tokens/$', AuthTokenList.as_view(), name='tokens'),
)
