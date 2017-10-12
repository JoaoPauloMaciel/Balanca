
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^balanca/', include('balanca.urls')),
    url(r'^autenticacao/', include('autenticacao.urls')),
]
