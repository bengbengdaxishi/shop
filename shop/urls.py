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
    url(r'^cart/(?P<uid>\d+)/$', view_car, name='view_car'),
    url(r'^detail/$', detail, name='datail'),
    url(r'^clean/(?P<cid>\d+)/$', cleanCart, name='cleanCart'),
    url(r'^all_goods/$', all_goods, name='all_goods'),
    url(r'^add_cart/(?P<uid>\d+)/(?P<chid>\d+)/(?P<fur_count>\d+)/$', add_cart, name='add_cart'),
]
