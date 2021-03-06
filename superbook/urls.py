"""superbook URL Configuration

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
from django.urls import path, include

import debug_toolbar

from rest_framework.documentation import include_docs_urls

from profiles.views import HomePage


admin.site.site_header = "SuperBook Secret Area"

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('playaway5DMN/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('users/', include('profiles.urls')),
    path('forms/', include('formschapter.urls', namespace='formschapter')),
    path('api/posts/', include('viewschapter.urls', namespace='viewschapter')),
    path('', include('viewschapter.urls', namespace='viewschapter')),
    path('api-docs/', include_docs_urls(title = 'Website API interface')),
    path('__debug__/', include(debug_toolbar.urls)),
]   
