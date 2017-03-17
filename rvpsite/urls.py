from django.conf.urls import url, include
from django.contrib import admin
from django.http import HttpResponse
from rvpsite.core import views as rvpsite_views
from rvpsite.contact.views import contact
from rvpsite.blog.views import blog, one_blog
from rvpsite.client.views import clients, clients_tmp

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', rvpsite_views.home, name='home'),
    url(r'^area/$', rvpsite_views.area, name='area'),
    url(r'^representadas/$', rvpsite_views.representations, name='representations'),
    url(r'^clientes/$', clients, name='clients'),
    url(r'^clientes_novo/$', clients_tmp, name='new_clients'), # desenvolvimento
    url(r'^noticias(?:/(?P<category>[\w-]*)(?:/(?P<page>[\w]*))?)?/$', blog, name='blog'),
    url(r'^s3direct/', include('s3direct.urls')),
    url(r'^contato/$', contact, name='contact'),
    url(r'^robots.txt', lambda x: HttpResponse("User-Agent: *\nDisallow: /clientes/\nDisallow: /clientes_novo/",
                                               content_type="text/plain"), name="robots_file"),
]
