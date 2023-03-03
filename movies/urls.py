"""movies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title= "Movie API",
        default_version="v1",
        description="API para recordar Djando y buscar trabajo",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="linderhassinger00@gmail.com"),
        license=openapi.License(name="MIT")
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', include("movie.urls")),
    path('swagger/', schema_view.with_ui("swagger", cache_timeout=0), name="swagger-docs"),
    #path('swagger.json/', schema_view.with_ui(cache_timout=0), name="swagger")
   
]
