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
from vohni.views import JourneyDetailView
from blog.views import PostsListView, PostDetailView 
from .settings import MEDIA_ROOT, DEBUG

urlpatterns = [
    url(r'^$', 'vohni.views.main_page', name='home'),
    url(r'^journeys/$', 'vohni.views.journeys', name='journeys'),
    url(r'^journeys/(?P<pk>\d+)/details/$', JourneyDetailView.as_view(),
    	name='details'),
#    url(r'^blog/$', 'vohni.views.blog', name='blog'),
    url(r'^team/$', 'vohni.views.team', name='team'),
    url(r'^blog/$', PostsListView.as_view(), name='blog'),
    url(r'^blog/(?P<pk>\d+)/$', PostDetailView.as_view()),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += patterns('',
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
)

if DEBUG:
    # serve files from media folder
    urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': MEDIA_ROOT}))