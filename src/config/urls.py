from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/', include('loginas.urls')),

    url(r'^api/projects/', include('apps.projects.api.urls')),
    url(r'^api/auth/', include('rest_auth.urls')),
]
