from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite_app import views

from mysite.views import current_datetime
urlpatterns = patterns('',
(r'', current_datetime),
)

#urlpatterns = patterns('',
    # Example:
    # (r'^mysite/', include('mysite.apps.foo.urls.foo')),
    # Uncomment this for admin:
    # (r'^admin/', include('django.contrib.admin.urls')),
 #   )
#urlpatterns = patter('',
    # Examples:
   # url(r'^mysite_app/', views.index, name='index')
    #url(r'^$', 'C:\Users\ANKITA\PycharmProjects\untitled\web2py\m2\login.html', name='home'),
    # url(r'^blog/', include('blog.urls')),

   # url(r'^admin/', include(admin.site.urls)),
#)




