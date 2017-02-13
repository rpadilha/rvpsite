from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse
from rvpsite.core import views as rvpsite_views
from rvpsite.contact.views import contact
from rvpsite.client.views import clients

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', rvpsite_views.home, name='home'),
    url(r'^area/', rvpsite_views.area, name='area'),
    url(r'^representadas/', rvpsite_views.representations, name='representations'),
    url(r'^clientes/', clients, name='clients'),
    url(r'^noticias/', rvpsite_views.blog, name='blog'),
    url(r'^contato/', contact, name='contact'),
    url(r'^robots.txt', lambda x: HttpResponse("User-Agent: *\nDisallow: /clientes/",
                                               content_type="text/plain"), name="robots_file"),
]
