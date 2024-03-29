"""cinda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from .views import Index, Login, Logout, Landing, LoadImagesAPI
from django.conf.urls.static import static

urlpatterns = [
    path('', Landing.as_view(), name='landing'),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('dashboard/', Index.as_view(), name='index'),
    path('upload-images/', LoadImagesAPI.as_view(), name='load-images'),
    path('admin/', admin.site.urls),
    path('dashboard/usuarios/', include('apps.users.urls', namespace='users')),
    path('dashboard/comunidades/', include('apps.comunidades.urls', namespace='comunidades')),
    path('markdownx/', include('markdownx.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
