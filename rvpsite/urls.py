from django.conf.urls import url
from django.contrib import admin
from rvpsite.core import views as rvpsite_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', rvpsite_views.home),
]
