from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers, serializers
from orders import views


router = routers.DefaultRouter()
router.register(r'orders', views.OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
