from django.conf.urls import include, url
from django.contrib import admin
from shoping.views import *
from shop.settings import MEDIA_ROOT
from django.views.static import serve
urlpatterns = [
    # Examples:
    # url(r'^$', 'shop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('^$', index, name='index'),
    url(r'^media/(?P<path>.*)$',  serve, {"document_root":MEDIA_ROOT}),
    # url(r'^cart/(?P<uid>\d+)/$', view_car, name='view_car'),
    url(r'^cart/$', view_cart, name='view_cart')
]
