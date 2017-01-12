from django.conf.urls import url
from django.contrib import admin
from rvpsite.core import views as rvpsite_views
from rvpsite.register.views import register

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', rvpsite_views.home, name='home'),
    url(r'^area/', rvpsite_views.area, name='area'),
    url(r'^representadas/', rvpsite_views.representations, name='representations'),
    url(r'^clientes/', rvpsite_views.clients, name='clients'),
    url(r'^cadastro/', register),
]
