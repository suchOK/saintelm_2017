"""saintelm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, patterns, include
from django.contrib import admin
from vohni.views import JourneyDetailView, EmailCreateView, JourneyListView
from blog.views import PostsListView, PostDetailView 
from .settings import MEDIA_ROOT, DEBUG

urlpatterns = [
    url(r'^$', 'vohni.views.main_page', name='home'),
    url(r'^journeys/$', JourneyListView.as_view(), name='journeys'),
    url(r'^journeys/(?P<slug>[\w-]+)/$', JourneyDetailView.as_view(),
    	name='details'),
    url(r'^confirm/$', EmailCreateView.as_view(), name='confirm'),
    url(r'^blog/$', PostsListView.as_view(), name='blog'),
    url(r'^blog/(?P<slug>[\w-]+)/$', PostDetailView.as_view(), name='posts'),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += patterns('',
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
    url(r'^tinymce/', include('tinymce.urls')),
)

if DEBUG:
    # serve files from media folder
    urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': MEDIA_ROOT}))