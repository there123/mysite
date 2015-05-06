#coding:utf-8
# URLconf文件--绑定视图函数和URL
# URLconf本质是 URL 模式以及要为该 URL 模式调用的视图函数之间的映射表
from django.conf.urls import include, url, patterns
from django.contrib import admin

from mysite.views import hello,home,current_datetime,hours_ahead

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',home),
    url(r'^admin/', include(admin.site.urls)),
    url('^hello/$',hello),
    url('^time/$',current_datetime),
    url(r'^time/plus/(\d{1,2})/$',hours_ahead),
]
#urlpatterns+=patterns('',)
