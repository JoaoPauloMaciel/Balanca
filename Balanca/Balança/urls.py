
from django.conf.urls import url, include
from rest_framework import routers
from balanca import views
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^balanca/', include('balanca.urls')),
    url(r'^autenticacao/', include('autenticacao.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_jwt_token),
]
