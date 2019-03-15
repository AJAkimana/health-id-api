"""healthid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from .apps.authentication.views import activate


admin.site.site_header = "HealthID Admin"
admin.site.site_title = "HealthID Admin"
admin.site.index_title = "Welcome to HealthID"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('healthid/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('activate/<uidb64>/<token>/', activate, name='activate')
]