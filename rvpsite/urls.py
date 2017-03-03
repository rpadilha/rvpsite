from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse
from rvpsite.core import views as rvpsite_views
from rvpsite.contact.views import contact
#from rvpsite.blog.views import blog
from rvpsite.client.views import clients, clients_tmp

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', rvpsite_views.home, name='home'),
    url(r'^area/$', rvpsite_views.area, name='area'),
    url(r'^representadas/$', rvpsite_views.representations, name='representations'),
    url(r'^clientes/$', clients, name='clients'),
    url(r'^clientes_novo/$', clients_tmp, name='clients_novo'), # desenvolvimento
    url(r'^noticias/$', rvpsite_views.blog, name='blog'),
    #url(r'^blog/(?P<slug>[\w-]+)/$', blog, name='blog_novo'), # desenvolvimento
    url(r'^contato/$', contact, name='contact'),
    url(r'^robots.txt', lambda x: HttpResponse("User-Agent: *\nDisallow: /clientes/\nDisallow: /clientes_novo/\nDisallow: /blog/*",
                                               content_type="text/plain"), name="robots_file"),
]
