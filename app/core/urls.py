"""core URL Configuration

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
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path("", include("index.urls"), name="index"),
    path("admin/", admin.site.urls),
    path("beer/", include("beer.urls"), name="beer"),
    path("brewery/", include("brewery.urls"), name="brewery"),
    path("image/", include("image.urls"), name="image"),
    path("location/", include("location.urls"), name="location"),
    path("user/", include("user.urls"), name="user"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Brews and Beers Admin"
admin.site.site_title = "Brews and Beers"
admin.site.index_title = "Admin Dashboard"
