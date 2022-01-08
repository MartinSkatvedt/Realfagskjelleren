"""rfkBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from inventoryManager import views as im_views
from users import views as user_views
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'products', im_views.ProductView)
router.register(r'merch', im_views.MerchView)
router.register(r'productcount', im_views.ProductCountView)
router.register(r'totalproductcount', im_views.TotalProductCountView)
router.register(r'users', user_views.UserView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('openid/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('accounts/', include('django.contrib.auth.urls')),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
